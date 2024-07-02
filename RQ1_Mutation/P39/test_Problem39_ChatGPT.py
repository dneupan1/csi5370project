# test file
import pytest
from Problem39_GeneratedSolution import removeInvalidParentheses  # Adjust this import based on your file structure

# Test with a string that's already valid
def test_already_valid():
    """
    A string with no invalid parentheses should return a list containing
    the original string itself, as no removals are necessary.
    """
    s = "abc(de)f"
    expected = ["abc(de)f"]
    assert sorted(removeInvalidParentheses(s)) == sorted(expected), "Failed with an already valid string"

# Test with a string needing removal of invalid parentheses in multiple ways
def test_multiple_removals():
    """
    A string with invalid parentheses that can be removed in multiple ways
    should return all unique valid strings.
    """
    s = "()())()"
    expected = ["()()()", "(())()"]
    assert sorted(removeInvalidParentheses(s)) == sorted(expected), "Failed with multiple removal options"

# Test with all characters being parentheses, needing removals
def test_all_parentheses():
    """
    A string composed entirely of parentheses, including some invalid, should
    return valid combinations after removals.
    """
    s = "(()"
    expected = ["()"]
    assert sorted(removeInvalidParentheses(s)) == sorted(expected), "Failed with all characters being parentheses"

# Test with mixed characters and parentheses
def test_mixed_characters():
    """
    A string with letters and parentheses, where some parentheses are invalid,
    should return correct valid strings after removals, without altering letters.
    """
    s = "a)b(c)d"
    expected = ["ab(c)d"]
    assert sorted(removeInvalidParentheses(s)) == sorted(expected), "Failed with mixed characters and parentheses"

# Test with no parentheses
def test_no_parentheses():
    """
    A string with no parentheses at all should return a list containing
    the original string, as there's nothing to remove.
    """
    s = "abcd"
    expected = ["abcd"]
    assert sorted(removeInvalidParentheses(s)) == sorted(expected), "Failed with no parentheses"

# Test removing multiple unmatched parentheses
def test_multiple_unmatched():
    """
    A string with multiple unmatched parentheses should have them removed
    to form valid strings, showcasing the function's capability to handle
    complex cases.
    """
    s = "))(("
    expected = [""]
    assert sorted(removeInvalidParentheses(s)) == sorted(expected), "Failed with multiple unmatched parentheses"

