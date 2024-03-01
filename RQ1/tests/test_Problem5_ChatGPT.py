import pytest
from Problem5_GeneratedSolution import isMatch  # Adjust the import path as needed

def test_match_exact():
    """
    Test exact matching without special characters.
    """
    assert isMatch("hello", "hello") == True, "Exact match should return True"

def test_match_single_character_wildcard():
    """
    Test matching with '?' wildcard, which matches any single character.
    """
    assert isMatch("test", "te?t") == True, "Single character wildcard match should return True"
    assert isMatch("test", "te??") == True, "Multiple single character wildcard match should return True"

def test_match_zero_or_more_characters_wildcard():
    """
    Test matching with '*' wildcard, which matches zero or more characters.
    """
    assert isMatch("test", "te*") == True, "Zero or more characters wildcard match should return True"
    assert isMatch("test", "*est") == True, "Leading wildcard match should return True"
    assert isMatch("test", "t*t") == True, "Wildcard in the middle match should return True"

def test_no_match():
    """
    Test scenarios where strings should not match.
    """
    assert isMatch("test", "txt") == False, "Mismatch should return False"
    assert isMatch("test", "tes") == False, "Shorter pattern should return False"
    assert isMatch("test", "tests") == False, "Longer pattern should return False"

def test_match_empty_string():
    """
    Test matching with empty strings and patterns with wildcards.
    """
    assert isMatch("", "") == True, "Empty string and pattern should match"
    assert isMatch("", "*") == True, "Empty string should match pattern with '*' wildcard"
    assert isMatch("a", "?") == True, "Single character should match '?' wildcard"
    assert isMatch("", "?") == False, "Empty string should not match '?' wildcard"

def test_complex_patterns():
    """
    Test matching with complex patterns involving multiple '*' and '?' wildcards.
    """
    assert isMatch("abefcdgiescdfimde", "ab*cd?i*de") == True, "Complex pattern should match"

def test_edge_cases():
    """
    Test handling of edge cases, such as patterns starting with '*' or containing only wildcards.
    """
    assert isMatch("abc", "*") == True, "Universal wildcard '*' should match any string"
    assert isMatch("abc", "********") == True, "Multiple '*' wildcards should match any string"
    assert isMatch("abc", "???") == True, "Exact length '?' wildcards should match"
    assert isMatch("abc", "????") == False, "Longer '?' wildcards pattern should not match"
