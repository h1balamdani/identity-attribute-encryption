This repository showcases implementations of three essential cryptographic schemes using the Python [Charm-Crypto](https://github.com/JHUISI/charm) framework:
- **AES**: Symmetric encryption 
- **IBE**: Identity-Based Encryption 
- **ABE**: Attribute-Based Encryption (specifically CP-ABE) 

These implementations are designed for secure data handling in environments where confidentiality, identity binding, and fine-grained access control are required (e.g., eHealth systems).

---

## 📁 Repository Structure
.
├── install-charm.md      # Step-by-step tutorial for installing Charm-Crypto on Ubuntu 20.04
├── aes.py                # AES encryption/decryption class and example usage
├── ibe.py                # IBE encryption/decryption class and example usage
├── abe.py                # ABE encryption/decryption class and example usage
├── converter.py          # Charm-Crypto converter utilities
├── group.py              # Shared group definition for cryptographic operations
└── README.md             # This file

---

## 🧱 Requirements
- vmware (or any other hypervisor) 

---

## 🛠️ Installation
To install Charm-Crypto on Ubuntu 20.04 LTS, follow the instructions in [`install-charm.md`](./install-charm.md).

---

## 🧪 How to Use
Each file includes example functions demonstrating how to use the implemented class. You can import the classes or run the files directly.

### Shared Components
- `group.py`: Contains common group parameters used across different encryption schemes
- `converter.py`: Provides utility functions for converting between different data formats required by Charm-Crypto

---

## 🤝 Credits
- [Charm-Crypto by JHU](https://github.com/JHUISI/charm)
- [Installation guide](https://blog.csdn.net/qq_34902437/article/details/137404638)
