import pytest
from Problem3_GeneratedSolution import reverse  # Adjust the import path as needed

def test_reverse_positive():
    """
    Test reversing a positive number.
    """
    assert reverse(123) == 321, "Should reverse a positive number"

def test_reverse_negative():
    """
    Test reversing a negative number.
    """
    assert reverse(-123) == -321, "Should reverse a negative number"

def test_reverse_zero():
    """
    Test reversing zero.
    """
    assert reverse(0) == 0, "Zero should return zero"

def test_reverse_overflow():
    """
    Test reversing a number that would overflow.
    The maximum positive 32-bit signed integer is 2,147,483,647,
    so reversing a number that exceeds this limit should return 0.
    """
    assert reverse(2_147_483_648) == 0, "Should return 0 on overflow"
    assert reverse(-2_147_483_649) == 0, "Should return 0 on underflow"

def test_reverse_edge_cases():
    """
    Test edge cases, including the maximum and minimum 32-bit signed integers.
    """
    assert reverse(2_147_483_647) == 0, "Reversing max int should return 0 due to overflow"
    assert reverse(-2_147_483_648) == 0, "Reversing min int should return 0 due to underflow"

def test_reverse_large_number_no_overflow():
    """
    Test reversing a large number that does not cause an overflow.
    """
    assert reverse(1_234_567_890) == 98_765_432_1, "Should reverse a large number without overflow"
