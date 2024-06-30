import pytest
from Problem17_GeneratedSolution import countSmaller  # Assuming the function 'countSmaller' is defined in 'solution.py'

@pytest.mark.parametrize("nums, expected", [
    # Example 1: Mixed numbers
    ([5, 2, 6, 1], [2, 1, 1, 0]),
    # Example 2: Single negative number
    ([-1], [0]),
    # Example 3: Two identical negative numbers
    ([-1, -1], [0, 0]),
    # Edge case: Empty array
    ([], []),
    # All elements in increasing order
    ([1, 2, 3, 4], [0, 0, 0, 0]),
    # All elements in decreasing order
    ([4, 3, 2, 1], [3, 2, 1, 0]),
    # Array with duplicates and negatives
    ([2, 9, 5, 4, 8, 1, 1], [2, 4, 2, 1, 2, 0, 0]),
    # Mixed positive and negative numbers
    ([10, -10, 11, 20, -20, 15], [4, 1, 2, 2, 0, 1]),
    # Array with single element
    ([3], [0]),
    # Array with all identical elements
    ([7, 7, 7, 7], [0, 0, 0, 0])
])
def test_countSmaller(nums, expected):
    """
    Tests the countSmaller function with various arrays to ensure it correctly counts the number of smaller elements to the right for each element.

    This test function verifies:
    - Proper handling of arrays with mixed, positive, and negative numbers.
    - Edge cases such as empty arrays and single-element arrays.
    - Correct counting of smaller elements to the right for arrays in increasing and decreasing order.
    - Arrays with duplicates to ensure the function handles identical values correctly.
    
    Args:
    nums (list of int): The input array of integers.
    expected (list of int): The expected array of counts of smaller elements to the right.
    """
    result = countSmaller(nums)
    assert result == expected, f"Test failed for nums={nums}. Expected {expected}, got {result}"
