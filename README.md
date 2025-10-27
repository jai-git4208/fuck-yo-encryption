# 🖕 FuckYou Crypto - Python Package

A secure encryption library that encodes your data using only F, U, C, K, Y, O characters. Maximum security with maximum attitude.

## 📦 Package Structure

```
fuckyou-crypto/
├── fuckyou_crypto/
│   ├── __init__.py
│   ├── core.py           # Main encryption/decryption logic
│   ├── encoder.py        # FUCKYOU base64 encoding
│   ├── noise.py          # Noise obfuscation
│   └── cli.py            # Command-line interface
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   ├── test_encoder.py
│   └── test_noise.py
├── examples/
│   └── basic_usage.py
├── setup.py
├── pyproject.toml
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

## 🚀 Installation

```bash
pip install fuckyou-crypto
```

## 💻 Usage

### Basic Encryption

```python
from fuckyou_crypto import encrypt, decrypt

# Encrypt with random key
result = encrypt("secret message")
print(result['camo'])  # FUCKYOUFUCKYOU...
print(result['key'])   # Save this!

# Decrypt
plaintext = decrypt(result['camo'], result['key'])
```

### Password-Based Encryption

```python
from fuckyou_crypto import encrypt, decrypt

# Encrypt with password
result = encrypt("secret message", password="mypassword")
print(result['camo'])
print(result['salt'])  # Save with password

# Decrypt
plaintext = decrypt(
    result['camo'], 
    password="mypassword",
    salt=result['salt']
)
```

### With Noise Obfuscation

```python
result = encrypt("secret", add_noise=True)
print(result['noise_positions'])  # Save these!

plaintext = decrypt(
    result['camo'],
    result['key'],
    noise_positions=result['noise_positions']
)
```

## 🖥️ CLI Usage

```bash
# Encrypt a message
fuckyou encrypt "hello world" --password mypass

# Encrypt from file
fuckyou encrypt --file input.txt --output encrypted.fu

# Decrypt
fuckyou decrypt "FUCKYOUFUCK..." --password mypass

# Add noise
fuckyou encrypt "secret" --noise --password mypass
```

## 🔒 Security Features

- **AES-128 CBC** via Fernet symmetric encryption
- **PBKDF2-SHA256** with 480,000 iterations
- **Random noise injection** for pattern obfuscation
- **FUCKYOU alphabet** camouflage encoding

## 📝 Package Files

### setup.py
```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fuckyou-crypto",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Secure encryption with FUCKYOU encoding",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/fuckyou-crypto",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Security :: Cryptography",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "cryptography>=41.0.0",
    ],
    entry_points={
        "console_scripts": [
            "fuckyou=fuckyou_crypto.cli:main",
        ],
    },
)
```

### pyproject.toml
```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_backend"

[project]
name = "fuckyou-crypto"
version = "1.0.0"
description = "Secure encryption with FUCKYOU encoding"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
keywords = ["encryption", "cryptography", "security", "obfuscation"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Topic :: Security :: Cryptography",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]
dependencies = [
    "cryptography>=41.0.0",
]

[project.urls]
Homepage = "https://github.com/yourusername/fuckyou-crypto"
Documentation = "https://github.com/yourusername/fuckyou-crypto#readme"
Repository = "https://github.com/yourusername/fuckyou-crypto"
Issues = "https://github.com/yourusername/fuckyou-crypto/issues"

[project.scripts]
fuckyou = "fuckyou_crypto.cli:main"
```

### README.md
```markdown
# 🖕 FuckYou Crypto

**Military-grade encryption that looks like spam.**

Encrypt your sensitive data using only the letters F, U, C, K, Y, O. 
Your encrypted messages will look like profanity-laden gibberish while 
maintaining industry-standard AES-128 security.

## Why?

- ✅ Actual secure encryption (Fernet/AES-128)
- ✅ Password-based key derivation (PBKDF2)
- ✅ Optional noise obfuscation
- ✅ Looks completely unprofessional
- ✅ Perfect for making security fun

## Quick Start

```bash
pip install fuckyou-crypto
```

```python
from fuckyou_crypto import encrypt, decrypt

# Encrypt
result = encrypt("my secret", password="p@ssw0rd")
print(result['camo'])  # FUCKYOUFUCKYOUFUCK...

# Decrypt
plaintext = decrypt(result['camo'], password="p@ssw0rd", salt=result['salt'])
```

## Features

### 🔐 Secure by Default
Uses industry-standard Fernet encryption (AES-128 in CBC mode with HMAC).

### 🔑 Password or Key
Choose between random key generation or password-based encryption with PBKDF2.

### 🎭 Noise Obfuscation
Add random characters to break up patterns and confuse frequency analysis.

### 🖕 FUCKYOU Encoding
All encrypted data uses only: F, U, C, K, Y, O (and lowercase variants).

## CLI Usage

```bash
# Encrypt with password
fuckyou encrypt "hello world" -p mypassword

# Encrypt file
fuckyou encrypt -f document.txt -o encrypted.fu -p mypassword

# Decrypt
fuckyou decrypt "FUCKYOUFUCK..." -p mypassword -s "base64salt=="

# Add noise
fuckyou encrypt "secret" -p mypassword --noise
```

## API Reference

### encrypt(plaintext, password=None, add_noise=False)

Encrypts plaintext message.

**Parameters:**
- `plaintext` (str): Message to encrypt
- `password` (str, optional): Password for encryption. If None, generates random key
- `add_noise` (bool): Whether to add noise obfuscation

**Returns:** Dict with keys:
- `camo`: Encrypted FUCKYOU-encoded string
- `key_info`: Encryption key (if no password) or None
- `salt`: Salt for password (if password used)
- `noise_positions`: List of noise positions (if noise used)
- `uses_password`: Boolean
- `has_noise`: Boolean

### decrypt(camo, key_or_password, salt=None, noise_positions=None, is_password=False)

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
- PBKDF2 with 480,000 iterations
- Cryptographically secure random number generation

🔒 **Keep your keys/passwords safe!** Losing them means losing your data.

🎭 **Noise is optional** but recommended for additional obfuscation.

## License

MIT License - see LICENSE file

## Contributing

PRs welcome! Please include tests and keep the attitude.

## Disclaimer

This is a real encryption library with a joke wrapper. Use responsibly.
Don't encrypt anything you can't afford to lose.

---

Made with 🖕 and ❤️
```

### requirements.txt
```
cryptography>=41.0.0
```

### LICENSE (MIT)
```
MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🎯 Next Steps

1. **Create GitHub repo**: `fuckyou-crypto`
2. **Organize code** into the package structure above
3. **Write tests** using pytest
4. **Build package**: `python -m build`
5. **Test locally**: `pip install -e .`
6. **Publish to PyPI**: `twine upload dist/*`
7. **Create releases** with version tags

## 📈 Marketing Ideas

- **Tagline**: "Military-grade encryption with maximum disrespect"
- **Tweet**: "Finally, a crypto library that matches my attitude 🖕"
- **Reddit**: Post on r/Python, r/shittyprogramming (ironically)
- **Dev.to article**: "Building Secure Encryption with a Middle Finger"
- **Badges**: Add to README (PyPI version, downloads, license)

## 🎨 Bonus Features to Add Later

- Web API wrapper
- Encryption of files/images
- Multi-language support (Spanish: "CHINGATU", etc.)
- Browser extension
- Mobile app
- Custom alphabet generation
- Streaming encryption for large files

Let's ship this! 🚀