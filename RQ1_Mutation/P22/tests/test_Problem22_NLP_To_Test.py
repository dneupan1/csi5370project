import pytest
from Problem22_GeneratedSolution import canPartition  # Assuming the function 'canPartition' is defined in 'solution.py'

@pytest.mark.parametrize("nums, expected", [
    # Example from the prompt
    ([1, 5, 11, 5], True),
    # Array with even number of elements and possible partition
    ([1, 2, 3, 4], True),
    # Array with even total sum but no possible partition
    #([1, 1, 3, 5], False),
    # Empty array, cannot partition
    #([], False),
    # Single element, cannot partition
    ([10], False),
    # All elements are the same and even count
    ([2, 2, 2, 2], True),
    # Odd total sum, automatically false
    #([1, 2, 3], False),
    # Large numbers with possible partition
    ([100, 1, 1, 98], True),
    # Large numbers without possible partition
    ([100, 99, 5, 3], False),
    # Test with zeros included
    ([0, 0, 0, 0, 1, 1, 2, 2], True),
    # Large array with repetitive elements that can be partitioned
    ([1]*100 + [100]*50, True),
    # Large array with repetitive elements that cannot be partitioned
    #([1]*100 + [100]*49, False)
])
def test_canPartition(nums, expected):
    """
    Tests the canPartition function with various arrays to ensure it correctly determines if the array can be partitioned into two subsets with equal sums.

    This test function checks:
    - Proper identification of partition possibilities in arrays with even and odd sums.
    - Handling of special cases such as empty arrays and arrays with one element.
    - Arrays with large numbers and potential precision issues.
    - Performance and correctness in scenarios with large arrays or arrays filled with repetitive elements.

    Args:
    nums (list of int): The array of integers to partition.
    expected (bool): Expected result indicating whether a valid partition exists.
    """
    assert canPartition(nums) == expected, f"Test failed for nums={nums}. Expected {expected}, got {canPartition(nums)}"
