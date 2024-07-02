import pytest
from Problem28_GeneratedSolution import firstMissingPositive as find_smallest_missing_positive  # Assuming the function 'find_smallest_missing_positive' is defined in 'solution.py'

@pytest.mark.parametrize("nums, expected", [
    # Example 1: Basic test with small array
    ([1, 2, 0], 3),
    # Example 2: Contains negative numbers and missing smallest positive integer
    ([3, 4, -1, 1], 2),
    # Example 3: All numbers are large and positive, smallest missing is 1
    ([7, 8, 9, 11, 12], 1),
    # Edge case: Contains only one negative number
    ([-1], 1),
    # Edge case: Empty array should return 1
    ([], 1),
    # Contains multiple missing numbers, smallest is 2
    ([1, 3, 4, 5], 2),
    # Test with zero and positive numbers only
    ([0, 5, 6, 1], 2),
    # No missing numbers, smallest missing is next after max
    ([1, 2, 3], 4),
    # Large array with no missing numbers within the range
    (list(range(1, 101)), 101),
    # Large array with gaps
    ([1, 2, 4, 6, 7, 10], 3),
    # Negative numbers and zero only
    ([-2, -3, 0], 1),
    # All numbers are the same
    ([2, 2, 2, 2], 1),
    # Mixed negative numbers and positives but no 1
    ([-1, 3, 4, -2, 5], 1)
])
def test_find_smallest_missing_positive(nums, expected):
    """
    Tests the find_smallest_missing_positive function with various configurations of integer arrays to ensure it correctly identifies the smallest missing positive integer.

    This test function verifies:
    - Proper handling of arrays with negative numbers, zeros, and positive numbers.
    - Correct detection of missing integers in sparse and dense arrays.
    - Special cases such as empty arrays, single-element arrays, and arrays with duplicate elements.

    Args:
    nums (list of int): The array of integers to analyze.
    expected (int): The expected result indicating the smallest missing positive integer.
    """
    assert find_smallest_missing_positive(nums) == expected, f"Test failed for input {nums}. Expected {expected}, got {find_smallest_missing_positive(nums)}"
