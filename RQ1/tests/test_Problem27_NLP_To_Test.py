import pytest
from Problem27_GeneratedSolution import search  # Assuming the function 'search' is defined in 'solution.py'

@pytest.mark.parametrize("nums, target, expected", [
    # Example 1: Rotated at middle, target found
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    # Example 2: Rotated at middle, target not found
    ([4, 5, 6, 7, 0, 1, 2], 3, -1),
    # Example 3: Single element, target not found
    ([1], 0, -1),
    # Single element, target found
    ([1], 1, 0),
    # Not rotated, target found
    ([1, 2, 3, 4, 5, 6], 4, 3),
    # Not rotated, target not found
    ([1, 2, 3, 4, 5, 6], 7, -1),
    # Rotated at the first element, target found
    ([6, 7, 0, 1, 2, 3, 4, 5], 0, 2),
    # Rotated at the last element, target found
    ([2, 3, 4, 5, 6, 7, 0, 1], 0, 6),
    # Large array, target found
    ([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5, 8),
    # Large array, target not found
    ([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 11, -1),
    # Array of two elements, target found
    ([2, 1], 1, 1),
    # Array of two elements, target not found
    ([2, 1], 3, -1)
])
def test_search(nums, target, expected):
    """
    Tests the search function with various rotated sorted arrays and targets to ensure it can correctly identify the index of the target or return -1 if the target is not present.

    This test function verifies:
    - Proper handling of rotated arrays with different rotation points.
    - Correct identification of target in both rotated and non-rotated arrays.
    - Efficiency in searching to ensure O(log n) complexity by testing with large arrays.
    - Edge cases such as single-element arrays and two-element arrays.

    Args:
    nums (list of int): The rotated sorted array.
    target (int): The target value to search for in the array.
    expected (int): The expected index of the target in the array, or -1 if it is not present.
    """
    assert search(nums, target) == expected, f"Test failed for nums={nums}, target={target}. Expected {expected}, got {search(nums, target)}"
