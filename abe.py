from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, pair
from charm.toolbox.secretutil import SecretUtil
from charm.toolbox.symcrypto import SymmetricCryptoAbstraction
from charm.toolbox.ABEnc import ABEnc
from charm.schemes.abenc.abenc_lsw08 import KPabe
from charm.core.math.pairing import hashPair as extractor
import hashlib
from modules_chiffrements.group import group

debug = False
MASTER_KEY = "SuperSecureMasterKey"

class EKPabe(ABEnc):
    def __init__(self, groupObj, verbose=False):
        ABEnc.__init__(self)
        global group, util
        group = groupObj
        util = SecretUtil(group, verbose)

    def derive_secret(self, attr):
        """Deterministically derive a secret using MASTER_KEY and attribute name."""
        hash_value = hashlib.sha256((MASTER_KEY + attr).encode()).hexdigest()
        return group.hash(hash_value, ZR)

    def setup(self):
        """Setup function that initializes public and master keys."""
        s = group.hash(MASTER_KEY, ZR)
        g = group.hash(MASTER_KEY, G1)
        return (g ** s, s)  # (Public Key, Master Key)

    def keygen(self, pk, mk, entity_attributes, policy_str):
        """Generates a secret key for a user based on their attributes."""
        policy = util.createPolicy(policy_str)
        attr_list = util.getAttributeList(policy)

        shares = util.calculateSharesDict(mk, policy)
        d = {}
        for x in attr_list:
            y = util.strip_index(x)
            if y in entity_attributes:  # Only include attributes the entity possesses
                d[y] = shares[x] / self.derive_secret(y)

        return {'policy': policy_str, 'Du': d}  # Return key structure

    def encrypt(self, pk, M, policy_str):
        """Encrypts a message under a policy instead of direct attributes."""
        policy = util.createPolicy(policy_str)
        attr_list = util.getAttributeList(policy)

        k = group.random(ZR)
        Cs = pk ** k

        # Generate Ci values for the attributes in the policy
        Ci = {attr: (group.hash(MASTER_KEY, G1) ** self.derive_secret(attr)) ** k for attr in attr_list}

        symcrypt = SymmetricCryptoAbstraction(extractor(Cs))
        C = symcrypt.encrypt(M)

        return {'C': C, 'Ci': Ci, 'policy': policy_str, 'attributes': attr_list}  # Include the policy in ciphertext

    def decrypt(self, entity_attributes, C, D):
        """Decrypts a ciphertext using the entity's attributes."""
        policy = util.createPolicy(D['policy'])
        attrs = util.prune(policy, entity_attributes)  # Match entity attributes with policy

        if attrs is False:
            return False  # Access denied

        coeff = util.getCoefficients(policy)
        prodT = 1
        for attr in attrs:
            x = attr.getAttribute()
            y = attr.getAttributeAndIndex()
            if x in D['Du'] and x in C['Ci']:
                prodT *= (C['Ci'][x] ** D['Du'][x]) ** coeff[y]

        symcrypt = SymmetricCryptoAbstraction(extractor(prodT))
        return symcrypt.decrypt(C['C'])

# Define group & scheme
kpabe = EKPabe(group)

def abe_encrypt(access_policy,plaintext_msg):

    plaintext_msg = plaintext_msg.encode()
    
    # Setup keys
    master_public_key, master_key = kpabe.setup()

    # Encrypt message under policy
    return kpabe.encrypt(master_public_key, plaintext_msg, access_policy)

def abe_decrypt(attributes,cipher_text):
    # Setup keys
    master_public_key, master_key = kpabe.setup()

    access_policy=cipher_text.get('policy')

    # Generate secret keys for each entity
    doctor_key = kpabe.keygen(master_public_key, master_key, attributes, access_policy)

    return kpabe.decrypt(attributes, cipher_text, doctor_key)

# # Define entity trying to decrypt
# doctor_user = ['DOCTOR']  # Should succeed
# nurse_user = ['NURSE']  # Should fail

# # Define policy for encryption
# access_policy = "(DOCTOR or TECHNICIAN)"
# plaintext_msg = "Confidential Medical Report".encode()

# # Attempt decryption
# print("second",abe_decrypt(access_policy,doctor_user, abe_encrypt(access_policy,"message")))  
