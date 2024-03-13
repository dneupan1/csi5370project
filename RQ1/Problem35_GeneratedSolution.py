


def palindromePairs(words):
    """
    Finds all unique palindrome pairs in the given list of words.
    
    :param words: List[str], a list of unique strings.
    :return: List[List[int]], a list of lists containing indices of palindrome pairs.
    """
    word_map = {word[::-1]: i for i, word in enumerate(words)}
    palindrome_pairs = []

    for i, word in enumerate(words):
        n = len(word)
        for j in range(n+1):
            # Split word into prefix and suffix
            prefix, suffix = word[:j], word[j:]
            
            # Check if prefix is a palindrome and suffix's reverse exists in word_map
            if prefix == prefix[::-1] and suffix in word_map and word_map[suffix] != i:
                palindrome_pairs.append([word_map[suffix], i])
            
            # Check if suffix is a palindrome and prefix's reverse exists in word_map
            # (j != n to avoid duplicate checks for whole word)
            if j != n and suffix == suffix[::-1] and prefix in word_map and word_map[prefix] != i:
                palindrome_pairs.append([i, word_map[prefix]])

    return palindrome_pairs

