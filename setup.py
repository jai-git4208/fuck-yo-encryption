from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fuckyou-crypto",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Secure encryption with FUCKYOU encoding - Military-grade security with maximum attitude",
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
        "Programming Language :: Python :: 3.13",
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
    keywords="encryption cryptography security obfuscation fuckyou",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/fuckyou-crypto/issues",
        "Source": "https://github.com/yourusername/fuckyou-crypto",
    },
)