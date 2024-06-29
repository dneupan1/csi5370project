def shortestPalindrome(s):
    """
    Converts a given string into the shortest palindrome by adding characters in front.
    
    Args:
    s (str): The input string.
    
    Returns:
    str: The shortest palindrome that can be formed by adding characters in front.
    
    Explanation:
    The function uses the KMP partial match table to determine the longest palindromic prefix.
    """
    def compute_kmp_table(s):
        """
        Computes the KMP partial match table for the given string.
        
        Args:
        s (str): The string for which to compute the KMP table.
        
        Returns:
        List[int]: The KMP table.
        """
        n = len(s)
        kmp_table = [0] * n
        j = 0  # length of the previous longest prefix suffix
        
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = kmp_table[j - 1]
            
            if s[i] == s[j]:
                j += 1
            
            kmp_table[i] = j
        
        return kmp_table
    
    # Edge case for an empty string
    if not s:
        return s
    
    # Construct the new string and its reverse with a special character in between
    temp = s + '#' + s[::-1]
    
    # Compute the KMP table for the new string
    kmp_table = compute_kmp_table(temp)
    
    # The length of the longest palindromic prefix
    longest_palindromic_prefix_len = kmp_table[-1]
    
    # Characters to be added in front
    to_add = s[longest_palindromic_prefix_len:][::-1]
    
    # Form the shortest palindrome
    shortest_palindrome = to_add + s
    
    return shortest_palindrome