# identity-attribute-encryption
A Python-based cryptography project implementing AES, Identity-Based Encryption (IBE), and Attribute-Based Encryption (ABE) using the Charm-Crypto library.

Great! Here's a clean and structured `README.md` that reflects your repository contents and guides users through your project:

---

# 🔐 AES, IBE, and ABE with Charm-Crypto in Python

This repository showcases implementations of three essential cryptographic schemes using Python:

- **AES**: Symmetric encryption using the [Charm-Crypto](https://github.com/JHUISI/charm) framework
- **IBE**: Identity-Based Encryption using Charm-Crypto
- **ABE**: Attribute-Based Encryption (specifically CP-ABE) using Charm-Crypto

These implementations are designed for secure data handling in environments where confidentiality, identity binding, and fine-grained access control are required (e.g., eHealth systems).

---

## 📁 Repository Structure

```
.
├── install-charm.md   # Step-by-step tutorial for installing Charm-Crypto on Ubuntu 20.04
├── aes.py             # AES encryption/decryption class and example usage
├── ibe.py             # IBE encryption/decryption class and example usage
├── abe.py             # ABE encryption/decryption class and example usage
└── README.md          # This file
```

---

## 🧱 Requirements

- vmware (or any other hypervisor) 

---

## 🛠️ Installation

To install Charm-Crypto on Ubuntu 20.04 LTS, follow the instructions in [`install-charm.md`](./install-charm.md).

---

## 🧪 How to Use

Each file includes example functions demonstrating how to use the implemented class. You can import the classes or run the files directly.

---

## 🤝 Credits

- [Charm-Crypto by JHU](https://github.com/JHUISI/charm)
- [Installation guide](https://blog.csdn.net/qq_34902437/article/details/137404638)
