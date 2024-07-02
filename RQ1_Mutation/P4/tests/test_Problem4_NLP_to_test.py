import pytest

from Problem4_GeneratedSolution import isMatch as is_match  # Assuming the function is defined in a file named solution.py

# Define test cases using the pytest framework
# Each test function is decorated with @pytest.mark

@pytest.mark.parametrize("s, p, expected", [
    # Basic examples
    ("aa", "a", False),    # Test matching exact characters without special symbols
    ("aa", "a*", True),    # Test '*' wildcard, matching multiple characters
    ("ab", ".*", True),    # Test '.*', matching any characters
    
    # More extensive testing of '.' and '*'
    ("aab", "c*a*b", True),  # '*' matching zero of 'c' and multiple 'a'
    ("mississippi", "mis*is*p*.", False),  # Multiple '*' and '.' characters
    
    # Edge cases
    ("", "", True),         # Both strings empty
    ("", ".*", True),       # Empty string matches with any pattern
    ("a", "", False),       # Non-empty string does not match empty pattern
    ("", "a*", True),       # Empty string matches zero occurrences of 'a'

    # Tests with no special characters
    ("hello", "hello", True),  # Direct match
    ("hello", "world", False), # Direct mismatch

    # Single character tests
    ("a", ".", True),         # Single '.' matches any single character
    ("", ".", False),         # '.' does not match empty string
    ("abc", "abc", True),     # Exact match
    ("abc", "ab.", True),     # '.' as any single character
    ("abc", "abcd", False),   # Mismatch with additional characters in pattern
])
def test_regex_matching(s, p, expected):
    """
    Test cases for regular expression matching.

    This function tests various combinations of input strings and patterns, checking
    if the function `is_match` behaves as expected. The parameters include:
    - s: input string
    - p: pattern string
    - expected: expected result (True or False)

    The use of `parametrize` allows for easy addition of new test cases.
    """
    assert is_match(s, p) == expected

# Note: You may add more cases as needed to ensure all logical branches in your 
# implementation are covered.
