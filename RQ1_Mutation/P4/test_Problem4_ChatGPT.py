import pytest
from Problem4_GeneratedSolution import isMatch  # Adjust the import path as needed

def test_match_exact():
    """
    Test exact matching without special characters.
    """
    assert isMatch("abc", "abc") == True, "Exact match should return True"

def test_match_single_character():
    """
    Test matching with '.' which should match any single character.
    """
    assert isMatch("abc", "a.c") == True, "Single character match should return True"

def test_match_zero_or_more():
    """
    Test matching with '*' which matches zero or more of the preceding element.
    """
    assert isMatch("abcccc", "abc*") == True, "Zero or more match should return True"
    assert isMatch("ab", "abc*") == True, "Zero occurrence match should return True"

def test_no_match():
    """
    Test scenarios where patterns do not match.
    """
    assert isMatch("abc", "abcd") == False, "Mismatch should return False"
    assert isMatch("abc", "a.d") == False, "Mismatch with single character should return False"

def test_match_empty_string():
    """
    Test matching with an empty string and pattern.
    """
    assert isMatch("", "") == True, "Empty string and pattern should match"
    assert isMatch("a", "") == False, "Non-empty string should not match empty pattern"
    assert isMatch("", "a*") == True, "Empty string should match pattern with zero occurrence"

def test_match_complex_patterns():
    """
    Test matching with complex patterns involving multiple '*' and '.' characters.
    """
    assert isMatch("aab", "c*a*b") == True, "Complex pattern should match"
    assert isMatch("mississippi", "mis*is*p*.") == False, "Complex pattern should not match"

def test_match_starting_star():
    """
    Test patterns that start with '*' which are technically invalid but should be handled.
    """
    assert isMatch("abc", "*abc") == False, "Pattern starting with '*' should not match"

def test_long_string():
    """
    Test with a longer string to check efficiency and correctness.
    """
    long_string = "a" * 50
    pattern = "a*" + "b"
    assert isMatch(long_string, pattern) == False, "Long string with non-matching pattern should return False"
