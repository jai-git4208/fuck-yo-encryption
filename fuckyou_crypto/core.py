"""
FuckYou Crypto - Core encryption/decryption functionality
"""

import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from .encoder import FuckYouEncoder
from .noise import add_noise, remove_noise

__version__ = "1.0.0"


class FuckYouCrypto:
    """Main encryption class using FUCKYOU encoding"""
    
    def __init__(self):
        self.encoder = FuckYouEncoder()
    
    def _derive_key_from_password(self, password: str, salt: bytes) -> bytes:
        """Derive encryption key from password using PBKDF2"""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,  # OWASP 2025 standard
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))
    
    def encrypt(self, plaintext: str, password: str = None, 
                add_noise_layer: bool = False) -> dict:
        """
        Encrypt plaintext using FUCKYOU encoding.
        
        Args:
            plaintext: Message to encrypt
            password: Optional password for encryption. If None, generates random key
            add_noise_layer: Whether to add noise obfuscation
            
        Returns:
            Dictionary containing:
                - camo: Encrypted FUCKYOU string
                - key_info: Key or None (if password used)
                - salt: Salt for password or None
                - noise_positions: List of noise positions or None
                - uses_password: Boolean
                - has_noise: Boolean
        """
        # Generate or derive key
        if password:
            salt = os.urandom(16)
            key = self._derive_key_from_password(password, salt)
            key_info = None
            salt_b64 = base64.urlsafe_b64encode(salt).decode()
        else:
            key = Fernet.generate_key()
            key_info = key.decode()
            salt = None
            salt_b64 = None
        
        # Encrypt with Fernet
        f = Fernet(key)
        token = f.encrypt(plaintext.encode())
        b64 = token.decode().rstrip("=")
        
        # Encode to FUCKYOU
        camo = self.encoder.encode(b64)
        
        # Add noise layer
        noise_positions = None
        if add_noise_layer:
            camo, noise_positions = add_noise(camo)
        
        return {
            'camo': camo,
            'key_info': key_info,
            'salt': salt_b64,
            'noise_positions': noise_positions,
            'uses_password': password is not None,
            'has_noise': add_noise_layer
        }
    
    def decrypt(self, camo: str, key_or_password: str, salt: str = None,
                noise_positions: list = None, is_password: bool = False) -> str:
        """
        Decrypt FUCKYOU encoded message.
        
        Args:
            camo: Encrypted FUCKYOU string
            key_or_password: Decryption key or password
            salt: Salt (required if password used)
            noise_positions: List of noise positions (if noise was used)
            is_password: Whether key_or_password is a password
            
        Returns:
            Decrypted plaintext string
        """
        # Remove noise if present
        if noise_positions:
            camo = remove_noise(camo, noise_positions)
        
        # Derive key if password was used
        if is_password:
            if not salt:
                raise ValueError("Salt is required when using password")
            salt_bytes = base64.urlsafe_b64decode(salt)
            key = self._derive_key_from_password(key_or_password, salt_bytes)
        else:
            key = key_or_password.encode()
        
        # Decode from FUCKYOU
        b64_no_pad = self.encoder.decode(camo)
        
        # Restore padding
        pad_len = (-len(b64_no_pad)) % 4
        b64_full = b64_no_pad + ("=" * pad_len)
        
        # Decrypt with Fernet
        f = Fernet(key)
        plaintext = f.decrypt(b64_full.encode())
        return plaintext.decode()


# Convenience functions
_crypto = FuckYouCrypto()

def encrypt(plaintext: str, password: str = None, add_noise: bool = False) -> dict:
    """
    Encrypt a message using FUCKYOU encoding.
    
    Args:
        plaintext: Message to encrypt
        password: Optional password. If None, uses random key
        add_noise: Whether to add noise obfuscation
        
    Returns:
        Dict with encrypted data and metadata
    """
    return _crypto.encrypt(plaintext, password, add_noise)


def decrypt(camo: str, key_or_password: str, salt: str = None,
            noise_positions: list = None, is_password: bool = False) -> str:
    """
    Decrypt a FUCKYOU encoded message.
    
    Args:
        camo: Encrypted FUCKYOU string
        key_or_password: Decryption key or password
        salt: Salt (required if password used)
        noise_positions: Noise positions (if noise was used)
        is_password: Whether key_or_password is a password
        
    Returns:
        Decrypted plaintext
    """
    return _crypto.decrypt(camo, key_or_password, salt, noise_positions, is_password)