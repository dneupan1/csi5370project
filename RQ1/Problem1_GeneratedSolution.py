

def length_of_longest_substring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.
    
    Args:
    s (str): The input string.
    
    Returns:
    int: The length of the longest substring without repeating characters.
    """
    # A set to keep track of the characters in the current window.
    chars = set()
    left = 0  # The start of the sliding window.
    max_length = 0  # The maximum length of substring found so far.
    
    for right in range(len(s)):
        # If the character at `right` is already in the set, 
        # it means we have found a repeating character.
        # So, we remove characters from the left until the repeating character is removed.
        while s[right] in chars:
            chars.remove(s[left])
            left += 1
        # Add the current character to the set and update the max_length if necessary.
        chars.add(s[right])
        max_length = max(max_length, right - left + 1)
        
    return max_length
