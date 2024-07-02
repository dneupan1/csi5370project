import pytest
from Problem3_GeneratedSolution import reverse as reverse_integer # Import the function from your module

# Test cases to check the reverse functionality and edge conditions

def test_positive_number():
    """Test reversing a positive number."""
    assert reverse_integer(123) == 321, "Should correctly reverse a positive integer"

def test_negative_number():
    """Test reversing a negative number."""
    assert reverse_integer(-123) == -321, "Should correctly reverse a negative integer"

def test_number_with_trailing_zeros():
    """Test reversing a number that ends with zeros."""
    assert reverse_integer(120) == 21, "Should correctly reverse a number with trailing zeros"

def test_zero():
    """Test reversing zero."""
    assert reverse_integer(0) == 0, "Should return zero for zero input"

def test_overflow_postive():
    """Test reversing a number that would cause overflow when positive."""
    assert reverse_integer(2**31 - 1) == 0, "Should return zero if reversed number exceeds positive limit"

def test_overflow_negative():
    """Test reversing a number that would cause overflow when negative."""
    assert reverse_integer(-2**31) == 0, "Should return zero if reversed number exceeds negative limit"

def test_max_int():
    """Test the edge case of the maximum int value."""
    assert reverse_integer(2147483647) == 0, "Should handle edge case of max int value"

def test_min_int():
    """Test the edge case of the minimum int value."""
    assert reverse_integer(-2147483648) == 0, "Should handle edge case of min int value"
