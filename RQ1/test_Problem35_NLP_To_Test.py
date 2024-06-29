def is_palindrome(word):
    """
    Helper function to check if a word is a palindrome.
    """
    return word == word[::-1]

def palindromePairs(words):
    """
    Finds all palindrome pairs in an array of unique strings.
    
    Args:
    words (List[str]): A list of unique strings.
    
    Returns:
    List[List[int]]: A list of pairs of indices where the concatenation of the words forms a palindrome.
    """
    word_map = {word: i for i, word in enumerate(words)}
    result = []
    
    for i, word in enumerate(words):
        n = len(word)
        for j in range(n + 1):
            prefix = word[:j]
            suffix = word[j:]
            
            # Check if prefix is a palindrome and the reverse of the suffix exists in the map
            if is_palindrome(prefix):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_map and word_map[reversed_suffix] != i:
                    result.append([word_map[reversed_suffix], i])
            
            # Check if suffix is a palindrome and the reverse of the prefix exists in the map
            # Check to avoid duplicates for the whole word being a palindrome
            if j != n and is_palindrome(suffix):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_map and word_map[reversed_prefix] != i:
                    result.append([i, word_map[reversed_prefix]])
    
    return result