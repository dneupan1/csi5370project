import pytest
from Problem38_GeneratedSolution import lengthOfLIS as length_of_LIS  # Assuming the function is named 'length_of_LIS' and is in 'solution.py'

@pytest.mark.parametrize("nums, expected", [
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),  # Example 1: General case with multiple options
    ([0, 1, 0, 3, 2, 3], 4),  # Example 2: Increasing subsequences with intermittent resets
    ([7, 7, 7, 7, 7, 7, 7], 1),  # Example 3: All elements are the same
    ([], 0),  # Edge case: Empty array should return 0
    ([1], 1),  # Single element array should return 1
    ([1, 3, 2], 2),  # Multiple possible subsequences, should pick the longest
    ([100, 90, 80, 70], 1),  # Strictly decreasing sequence
    ([1, 2, 3, 4, 5], 5),  # Strictly increasing sequence
    ([3, 10, 2, 1, 20], 3),  # Sequence with both increases and decreases
    ([10, 22, 9, 33, 21, 50, 41, 60, 80], 6),  # Complex mixed sequence
])
def test_length_of_LIS(nums, expected):
    """
    Tests the length_of_LIS function with various arrays to ensure it correctly calculates the length of the longest strictly increasing subsequence.

    This test function verifies:
    - The function's ability to handle arrays with unique scenarios, including strictly increasing, decreasing, and constant elements.
    - Edge cases such as empty and single-element arrays.
    - Proper calculation in scenarios with multiple valid subsequences.

    Args:
    nums (list of int): The input array of numbers.
    expected (int): The expected length of the longest strictly increasing subsequence.
    """
    assert length_of_LIS(nums) == expected, f"Test failed for input {nums}. Expected {expected}, but got {length_of_LIS(nums)}"
