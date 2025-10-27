"""
FUCKYOU Base64 Encoder - Maps base64 to FUCKYOU alphabet
"""

BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"


class FuckYouEncoder:
    """Encodes/decodes base64 strings to FUCKYOU alphabet"""
    
    def __init__(self):
        self.tokens = self._generate_tokens()
        self.enc_map = {b64: tok for b64, tok in zip(BASE64_ALPHABET, self.tokens)}
        self.dec_map = {tok: b64 for tok in self.tokens 
                        for b64, t in self.enc_map.items() if t == tok}
    
    def _generate_tokens(self) -> list:
        """Generate 64 unique 2-character tokens using FUCKYOU alphabet"""
        chars = ['F', 'U', 'C', 'K', 'Y', 'O', 'f', 'u']  # 8 chars = 64 combinations
        tokens = []
        
        for c1 in chars:
            for c2 in chars:
                tokens.append(c1 + c2)
                if len(tokens) >= 64:
                    break
            if len(tokens) >= 64:
                break
        
        return tokens
    
    def encode(self, b64str: str) -> str:
        """
        Encode a base64 string to FUCKYOU alphabet.
        
        Args:
            b64str: Base64 string (without padding)
            
        Returns:
            FUCKYOU encoded string
        """
        result = []
        for ch in b64str:
            if ch not in self.enc_map:
                raise ValueError(f"Invalid base64 character: {ch}")
            result.append(self.enc_map[ch])
        return "".join(result)
    
    def decode(self, camo: str) -> str:
        """
        Decode a FUCKYOU string back to base64.
        
        Args:
            camo: FUCKYOU encoded string
            
        Returns:
            Base64 string (without padding)
        """
        if len(camo) % 2 != 0:
            raise ValueError("FUCKYOU string length must be even (2-char tokens)")
        
        base64_chars = []
        for i in range(0, len(camo), 2):
            token = camo[i:i+2]
            if token not in self.dec_map:
                raise ValueError(f"Invalid FUCKYOU token: {token}")
            base64_chars.append(self.dec_map[token])
        
        return "".join(base64_chars)
    
    def get_alphabet(self) -> str:
        """Return the FUCKYOU alphabet"""
        return "FUCKYOfu"
    
    def get_tokens(self) -> list:
        """Return all 64 tokens"""
        return self.tokens.copy()