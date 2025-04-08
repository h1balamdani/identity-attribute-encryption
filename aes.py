from charm.toolbox.symcrypto import SymmetricCryptoAbstraction
from charm.toolbox.securerandom import OpenSSLRand
import base64

# def generate_aes_key():
#     Create an instance of OpenSSLRand
#     rand = OpenSSLRand()

#     Generate a 256-bit (32-byte) AES key using OpenSSLRand
#     return rand.getRandomBytes(32)  # AES-256

def generate_aes_key():
    # Create an instance of OpenSSLRand
    rand = OpenSSLRand()
    
    # Generate a 256-bit (32-byte) AES key using OpenSSLRand
    bytes= rand.getRandomBytes(32)  # AES-256
    return base64.b64encode(bytes).decode('utf-8')
#needed to do this in order to generate a string wich was essential for ibe to work ! (ibe sym key)

def aes_encrypt(key,plaintext):
    # Create a symmetric cipher object
    cipher = SymmetricCryptoAbstraction(key)

    # Encrypt
    ciphertext = cipher.encrypt(plaintext.encode())
    return base64.b64encode(ciphertext.encode())  # Convert to base64 for storage or transmission

def aes_decrypt(key,encoded_ciphertext):
    # Decrypt
    cipher = SymmetricCryptoAbstraction(key)
    decoded_ciphertext = base64.b64decode(encoded_ciphertext)  # Convert back from base64
    return cipher.decrypt(decoded_ciphertext).decode()

key = generate_aes_key()

encrypted_message = aes_encrypt(key,"message")
aes_decrypted_message = aes_decrypt(key,encrypted_message)

