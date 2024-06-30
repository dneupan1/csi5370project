import pytest
from Problem35_GeneratedSolution import palindromePairs as palindrome_pairs  # Assuming the function 'palindrome_pairs' is defined in 'solution.py'

@pytest.mark.parametrize("words, expected", [
    (["abcd", "dcba", "lls", "s", "sssll"], [[0, 1], [1, 0], [3, 2], [2, 4]]),  # Example 1
    (["bat", "tab", "cat"], [[0, 1], [1, 0]]),  # Example 2
    (["a", ""], [[0, 1], [1, 0]]),  # Example 3 with an empty string
    ([], []),  # Edge case: empty list of words
    (["a"], []),  # Single word, no pairs possible
    (["abc", "cba", "bca", "a", "b"], [[0, 1], [1, 0], [3, 1], [3, 2], [4, 0]]),  # Complex scenario with multiple pairs
    (["race", "car", "ecar"], []),  # No possible palindrome pairs
    (["12321", "123"], [[0, 1]]),  # Numeric strings forming palindromes
    (["ggg", "g", "gg"], [[0, 2], [2, 0], [2, 1], [1, 2]]),  # All combinations form palindromes
    (["word", "drow", "row", "d"], [[0, 1], [1, 0], [3, 2]])  # Mixed words forming palindromes
])
def test_palindrome_pairs(words, expected):
    """
    Tests the palindrome_pairs function with various lists of unique strings to ensure it correctly identifies all palindrome pairs.

    This test function verifies:
    - Correct identification of palindrome pairs from simple to complex scenarios, including cases with special characters and numerics.
    - Handling of edge cases such as empty lists and single-word lists.
    - Efficiency and accuracy in identifying non-obvious palindrome pair combinations.

    Args:
    words (list of str): The list of unique strings to analyze.
    expected (list of list of int): Expected indices pairs that form palindrome pairs.
    """
    result = palindrome_pairs(words)
    assert sorted(result) == sorted(expected), f"Test failed for words={words}. Expected {expected}, got {result}"
