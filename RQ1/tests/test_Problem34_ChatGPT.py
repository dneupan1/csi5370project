# test file
import pytest
from Problem34_GeneratedSolution import shortestPalindrome  # Adjust this import based on your file structure

# Test with an empty string
def test_empty_string():
    assert shortestPalindrome("") == "", "Failed to handle an empty string"

# Test with a string that is already a palindrome
def test_already_palindrome():
    assert shortestPalindrome("racecar") == "racecar", "Failed with a string that is already a palindrome"

# Test with a string needing one character added
def test_one_char_needed():
    assert shortestPalindrome("abcd") == "dcbabcd", "Failed with a string needing one character added"

# Test with a string needing multiple characters added
def test_multiple_chars_needed():
    assert shortestPalindrome("abc") == "cbabc", "Failed with a string needing multiple characters added"

# Test with a string where the entire string except one character forms a palindrome
def test_almost_all_chars_needed():
    assert shortestPalindrome("aacecaaa") == "aaacecaaa", "Failed with a string where the entire string except one character forms a palindrome"

# Test with single character strings
def test_single_char():
    assert shortestPalindrome("a") == "a", "Failed with a single character string"

# Test with a string of two different characters
def test_two_chars():
    assert shortestPalindrome("ab") == "bab", "Failed with a string of two different characters"

# Test with complex strings requiring extensive additions
def test_complex_string():
    assert shortestPalindrome("abcdefg") == "gfedcbabcdefg", "Failed with a complex string requiring extensive additions"

