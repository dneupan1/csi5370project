# test file
import pytest
from Problem28_GeneratedSolution import firstMissingPositive  # Adjust this import based on your file structure

# Test with a mix of positive and negative numbers, including the typical case
def test_mixed_numbers():
    nums = [3, 4, -1, 1]
    expected = 2
    assert firstMissingPositive(nums) == expected, "Failed with a mix of positive and negative numbers"

# Test with all positive numbers, including cases that require reordering
def test_all_positive():
    nums = [1, 2, 0]
    expected = 3
    assert firstMissingPositive(nums) == expected, "Failed with all positive numbers"

# Test with a case where the answer is in the middle of the array
def test_missing_middle():
    nums = [1, 2, 3, 5]
    expected = 4
    assert firstMissingPositive(nums) == expected, "Failed when the missing positive is in the middle"

# Test with negative numbers only, expecting 1 as the smallest missing positive
def test_negative_only():
    nums = [-1, -2, -3]
    expected = 1
    assert firstMissingPositive(nums) == expected, "Failed with negative numbers only"

# Test with an empty array, expecting 1 as the smallest missing positive
def test_empty_array():
    nums = []
    expected = 1
    assert firstMissingPositive(nums) == expected, "Failed with an empty array"

# Test with a single positive number, checking edge cases
def test_single_positive():
    nums = [1]
    expected = 2
    assert firstMissingPositive(nums) == expected, "Failed with a single positive number"

# Test with a single negative number, expecting 1 as the smallest missing positive
def test_single_negative():
    nums = [-1]
    expected = 1
    assert firstMissingPositive(nums) == expected, "Failed with a single negative number"

# Test with repeated numbers, to ensure the algorithm correctly identifies the missing smallest positive
def test_repeated_numbers():
    nums = [1, 1, 2, 2]
    expected = 3
    assert firstMissingPositive(nums) == expected, "Failed with repeated numbers"

# Test with numbers in correct sequence to check for n+1 case
def test_sequence_numbers():
    nums = [1, 2, 3, 4, 5]
    expected = 6
    assert firstMissingPositive(nums) == expected, "Failed with a correct sequence of numbers"

# Test with a large range of numbers, including negatives, to ensure scalability and performance
def test_large_range():
    nums = [-10, 1, 3, 5, -20, 2, 4]
    expected = 6
    assert firstMissingPositive(nums) == expected, "Failed with a large range of numbers"
