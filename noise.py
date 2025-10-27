"""
Noise obfuscation module for FuckYou Crypto
"""

import os


def add_noise(camo: str, noise_level: int = 5) -> tuple:
    """
    Add random FUCKYOU characters as noise to confuse pattern analysis.
    
    Args:
        camo: Original FUCKYOU encoded string
        noise_level: One noise char per this many chars (default: 5)
        
    Returns:
        Tuple of (noisy_string, noise_positions)
    """
    chars = ['F', 'U', 'C', 'K', 'Y', 'O', 'f', 'u']
    result = list(camo)
    positions = []
    
    # Calculate number of noise chars to add
    num_noise = len(camo) // noise_level
    
    # Generate all random positions first, then sort them
    # This way we can insert from left to right and track the offset
    temp_positions = []
    for _ in range(num_noise):
        pos = int.from_bytes(os.urandom(2), 'big') % (len(camo) + 1)
        temp_positions.append(pos)
    
    temp_positions.sort()
    
    # Insert noise characters, tracking cumulative offset
    offset = 0
    for original_pos in temp_positions:
        actual_pos = original_pos + offset
        noise_char = chars[int.from_bytes(os.urandom(1), 'big') % len(chars)]
        result.insert(actual_pos, noise_char)
        positions.append(actual_pos)
        offset += 1
    
    return ''.join(result), positions


def remove_noise(noisy_camo: str, positions: list) -> str:
    """
    Remove noise characters from the noisy camo text.
    
    Args:
        noisy_camo: FUCKYOU string with noise
        positions: List of noise character positions
        
    Returns:
        Clean FUCKYOU string
    """
    if not positions:
        return noisy_camo
    
    result = list(noisy_camo)
    
    # Sort positions in descending order to remove from end to start
    # This prevents index shifting issues
    for pos in sorted(positions, reverse=True):
        if 0 <= pos < len(result):
            result.pop(pos)
    
    return ''.join(result)


def calculate_noise_level(data_length: int, target_noise_chars: int) -> int:
    """
    Calculate appropriate noise level for desired number of noise chars.
    
    Args:
        data_length: Length of data to add noise to
        target_noise_chars: Desired number of noise characters
        
    Returns:
        Noise level parameter
    """
    if target_noise_chars <= 0:
        return 0
    return max(1, data_length // target_noise_chars)