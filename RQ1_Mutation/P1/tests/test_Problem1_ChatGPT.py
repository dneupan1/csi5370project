import pytest
from Problem1_GeneratedSolution import length_of_longest_substring
# Test with unique characters
def test_unique_characters():
    """
    Test a string with all unique characters.
    Expectation: The length of the string itself since all characters are unique.
    """
    assert length_of_longest_substring("abcde") == 5, "Failed on all unique characters"

# Test with repeating characters
@pytest.mark.parametrize("test_input,expected", [
    ("abcabcbb", 3),  # Repeating characters with the longest substring at the beginning
    ("bbbbb", 1),  # All characters are the same
    ("pwwkew", 3),  # Repeating characters with the longest substring in the middle
    ("", 0),  # Empty string
    ("au", 2),  # Two characters, unique
    ("dvdf", 3)  # Repeating character with the longest substring involving the last character
])
def test_repeating_characters(test_input, expected):
    """
    Test strings with repeating characters.
    The test cases cover various scenarios including longest substrings at different positions,
    an empty string, and strings with all characters being the same.
    """
    assert length_of_longest_substring(test_input) == expected, f"Failed on input: {test_input}"

# Test with a single character string
def test_single_character():
    """
    Test a string that contains a single character.
    Expectation: Length should be 1 as there's only one character.
    """
    assert length_of_longest_substring("a") == 1, "Failed on single character"

# Optionally, you can add more specific tests for edge cases, or to increase coverage if necessary.
