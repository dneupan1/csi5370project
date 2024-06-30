import pytest

from Problem5_GeneratedSolution import isMatch as is_match  # Assuming the function is defined in a file named solution.py

@pytest.mark.parametrize("s, p, expected", [
    # Basic examples
    ("aa", "a", False),    # Test basic mismatch without wildcards
    ("aa", "*", True),     # Test '*' wildcard matching entire string
    ("cb", "?a", False),   # Test '?' wildcard matching one character, not full string

    # Testing '?' and '*'
    ("abc", "a?c", True),  # '?' matches one character in the middle
    ("abc", "abc*", True), # '*' at the end can be empty
    ("abc", "*abc", True), # '*' at the start can be empty
    ("abc", "a*", True),   # '*' matches the rest of the string
    ("abc", "*d", False),  # '*' does not match if remaining characters differ
    ("abc", "???", True),  # '?' matches all characters individually

    # Edge cases
    ("", "", True),         # Both strings empty
    ("", "*", True),        # Empty string matches with '*' wildcard
    ("a", "", False),       # Non-empty string does not match empty pattern
    ("", "?", False),       # '?' does not match empty string

    # Complex patterns
    ("abefcdgiescdfimde", "ab*cd?i*de", True),  # Complex pattern with mixed wildcards

    # More edge cases
    ("hello", "he*o", True),  # '*' matches middle characters
    ("hello", "*l*", True),   # '*' matches multiple characters including 'l'
    ("hello", "he??o", True), # '??' matches two characters
    ("hello", "he???", False) # '???' too long to match
])
def test_wildcard_matching(s, p, expected):
    """
    Test cases for wildcard pattern matching.

    The function `is_match` is tested with various combinations of input strings
    (s) and patterns (p), each containing '?' and '*' wildcards. The expected results
    are indicated, and this test function ensures that the implemented function
    behaves as required by the problem description.

    Using `parametrize` ensures comprehensive testing with minimal code repetition,
    facilitating easy extension and maintenance of the test suite.
    """
    assert is_match(s, p) == expected

# Additional tests could be added here to ensure full coverage if the initial 
# implementation reveals uncovered code paths.
