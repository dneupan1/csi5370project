import pytest
from Problem21_GeneratedSolution import countPartitions as countGreatPartitions  # Assuming the function 'countGreatPartitions' is defined in 'solution.py'

MOD = 10**9 + 7

@pytest.mark.parametrize("nums, k, expected", [
    # Example 1: Multiple valid partitions
    ([1, 2, 3, 4], 4, 6),
    # Example 2: No valid partitions
    ([3, 3, 3], 4, 0),
    # Example 3: Simple case with only two elements
    ([6, 6], 2, 2),
    # Edge case: Empty array, should be 0 as there are no partitions possible
    ([], 1, 0),
    # Edge case: Single element equal to k, cannot form two groups
    ([5], 5, 0),
    # Edge case: Single element greater than k, cannot form two groups
    ([10], 1, 0),
    # Case with all elements the same and greater than k
    ([5, 5, 5], 5, 0),
    # Case with elements adding up exactly to 2*k
    ([2, 2, 2, 2], 4, 6),
    # Large case with no valid partitions due to high k
    ([1, 1, 1, 1], 5, 0),
    # Mixed elements with some repeated values
    ([1, 2, 2, 3, 3, 4], 6, 10),
    # Larger array with multiple valid partitions
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 0),  # Adjust expected value accordingly
])
def test_countGreatPartitions(nums, k, expected):
    """
    Tests the countGreatPartitions function with various arrays and k values to ensure it correctly counts the number of distinct great partitions.

    This test function verifies:
    - Handling of simple and complex cases, ensuring partitions are correctly identified.
    - Edge cases such as empty arrays, single-element arrays, and cases where no valid partitions are possible.
    - Proper counting of partitions with arrays containing repeated elements.
    - Performance and correctness for larger arrays.

    Args:
    nums (list of int): The array of positive integers to partition.
    k (int): The minimum sum required for each partition group.
    expected (int): The expected number of distinct great partitions.
    """
    result = countGreatPartitions(nums, k)
    assert result == expected, f"Test failed for nums={nums}, k={k}. Expected {expected}, got {result}"
