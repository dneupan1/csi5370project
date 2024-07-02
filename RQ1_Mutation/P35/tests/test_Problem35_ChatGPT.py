# test file
import pytest
from Problem35_GeneratedSolution import palindromePairs  # Adjust this import based on your file structure

# Test with a basic example where palindrome pairs are formed by appending
def test_basic_pairs():
    words = ["bat", "tab", "cat"]
    expected = [[0, 1], [1, 0]]  # "battab" and "tabbat" are palindromes
    assert sorted(palindromePairs(words)) == sorted(expected), "Failed with basic palindrome pairs"


# Test with words that are themselves palindromes
def test_self_palindrome():
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    expected = [[0, 1], [1, 0], [2, 4], [3, 2]]  # Includes "slls" and "llssssll"
    assert sorted(palindromePairs(words)) == sorted(expected), "Failed with words that are themselves palindromes"

# Test with no possible palindrome pairs
def test_no_pairs():
    words = ["abc", "def"]
    expected = []  # No palindrome pairs can be formed
    assert palindromePairs(words) == expected, "Failed with no possible palindrome pairs"

# Test with complex cases involving multiple palindrome pairs and overlaps
def test_complex_cases():
    words = ["a", "abc", "aba", ""]
    expected = [[0, 3], [3, 0], [2, 3], [3, 2]]  # "a" and "" make two pairs, "aba" and "" make two pairs
    assert sorted(palindromePairs(words)) == sorted(expected), "Failed with complex cases"

