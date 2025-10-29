#  FuckYou Crypto

**Military-grade encryption that looks like spam.**

Encrypt your sensitive data using only the letters F, U, C, K, Y, O. Your encrypted messages will look like profanity-laden gibberish while maintaining industry-standard AES-128 security.

![PyPI](https://img.shields.io/pypi/v/fuckyou_crypto)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Why?

- ✅ Actual secure encryption (Fernet/AES-128)
- ✅ Password-based key derivation (PBKDF2-SHA256, 480k iterations)
- ✅ Optional noise obfuscation
- ✅ Looks completely unprofessional
- ✅ Perfect for making security fun

## Installation

```bash
pip install fuckyou-crypto
```

## Quick Start

```python
from fuckyou_crypto import encrypt, decrypt

# Encrypt with password
result = encrypt("my secret message", password="p@ssw0rd")
print(result['camo'])  
# Output: FUCKYOUFUCKYOUFUCKYOU...

# Decrypt
plaintext = decrypt(
    result['camo'], 
    key_or_password="p@ssw0rd", 
    salt=result['salt'],
    is_password=True
)
print(plaintext)  # "my secret message"
```

## Features

### 🔐 Secure by Default
Uses industry-standard Fernet encryption (AES-128 in CBC mode with HMAC).

### 🔑 Password or Key
Choose between random key generation or password-based encryption with PBKDF2.

### 🎭 Noise Obfuscation
Add random characters to break up patterns and confuse frequency analysis.

### 🖕 FUCKYOU Encoding
All encrypted data uses only: **F, U, C, K, Y, O** (and lowercase variants).

## Usage Examples

### Basic Encryption (Random Key)

```python
from fuckyou_crypto import encrypt, decrypt

# Encrypt
result = encrypt("hello world")
print(f"Encrypted: {result['camo']}")
print(f"Key: {result['key_info']}")  # Save this!

# Decrypt
plaintext = decrypt(result['camo'], result['key_info'])
print(f"Decrypted: {plaintext}")
```

### Password-Based Encryption

```python
result = encrypt("secret data", password="mypassword")

# Save these:
print(f"Encrypted: {result['camo']}")
print(f"Salt: {result['salt']}")

# Decrypt
plaintext = decrypt(
    result['camo'],
    "mypassword",
    salt=result['salt'],
    is_password=True
)
```

### With Noise Obfuscation

```python
result = encrypt("secret", password="pass123", add_noise=True)

# Save these:
print(f"Encrypted: {result['camo']}")
print(f"Salt: {result['salt']}")
print(f"Noise positions: {result['noise_positions']}")

# Decrypt
plaintext = decrypt(
    result['camo'],
    "pass123",
    salt=result['salt'],
    noise_positions=result['noise_positions'],
    is_password=True
)
```

## API Reference

### `encrypt(plaintext, password=None, add_noise=False)`

Encrypts plaintext message.

**Parameters:**
- `plaintext` (str): Message to encrypt
- `password` (str, optional): Password for encryption. If None, generates random key
- `add_noise` (bool): Whether to add noise obfuscation

**Returns:** Dictionary with:
- `camo`: Encrypted FUCKYOU-encoded string
- `key_info`: Encryption key (if no password) or None
- `salt`: Salt for password (if password used) or None
- `noise_positions`: List of noise positions (if noise used) or None
- `uses_password`: Boolean
- `has_noise`: Boolean

### `decrypt(camo, key_or_password, salt=None, noise_positions=None, is_password=False)`

Decrypts FUCKYOU-encoded message.

**Parameters:**
- `camo` (str): Encrypted FUCKYOU string
- `key_or_password` (str): Decryption key or password
- `salt` (str, optional): Salt (required if password used)
- `noise_positions` (list, optional): Noise positions (if noise used)
- `is_password` (bool): Whether key_or_password is a password

**Returns:** Decrypted plaintext string

## Security Notes

⚠️ **This is real encryption!** Despite the silly encoding, this uses:
- AES-128 in CBC mode (via Fernet)
- HMAC for authentication
- PBKDF2 with 480,000 iterations (OWASP 2025 standard)
- Cryptographically secure random number generation

🔒 **Keep your keys/passwords safe!** Losing them means losing your data forever.

🎭 **Noise is optional** but recommended for additional obfuscation against pattern analysis.

## How It Works

1. **Encryption**: Your plaintext is encrypted using Fernet (AES-128)
2. **Base64 Mapping**: The resulting base64 is mapped to FUCKYOU alphabet
3. **Noise (Optional)**: Random FUCKYOU characters are injected
4. **Result**: A string that looks like "FUCKYOUFUCKYOU..." spam

The encoding is completely reversible with the correct key/password!

## Requirements

- Python 3.8+
- cryptography >= 41.0.0

## License

MIT License - see LICENSE file for details

## Contributing

PRs welcome! Please include tests and keep the attitude. 🖕

## Disclaimer

This is a real encryption library with a joke wrapper. Use responsibly.
Don't encrypt anything you can't afford to lose. The authors are not responsible
for any data loss, angry sysadmins, or raised eyebrows from security auditors.

## Support

If you encounter issues, please report them on GitHub:
https://github.com/jai-git4208/fuck-yo-encryption/issues

---

Made with 🖕 and ❤️ by Jaimin.

*"Finally, a crypto library that matches my attitude."*
