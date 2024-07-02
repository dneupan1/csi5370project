# test file
import pytest
from Problem27_GeneratedSolution import search  # Ensure this import matches the location of your function

# Test case for finding a target in a normally ordered array (no rotation)
def test_search_normally_ordered():
    nums = [1, 2, 3, 4, 5, 6, 7]
    target = 5
    expected = 4  # Target 5 is at index 4
    assert search(nums, target) == expected, "Failed to find target in a normally ordered array"

# Test case for finding a target in the left half of a rotated array
def test_search_left_half_rotated():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 5
    expected = 1  # Target 5 is at index 1 in this rotated array
    assert search(nums, target) == expected, "Failed to find target in the left half of a rotated array"

# Test case for finding a target in the right half of a rotated array
def test_search_right_half_rotated():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 1
    expected = 5  # Target 1 is at index 5 in this rotated array
    assert search(nums, target) == expected, "Failed to find target in the right half of a rotated array"

# Test case for target not found in the array
def test_search_target_not_found():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    expected = -1  # Target 3 is not in the array
    assert search(nums, target) == expected, "Failed to return -1 when target is not found"

# Test case for an empty array, expecting -1 as the target cannot be found
def test_search_empty_array():
    nums = []
    target = 1
    expected = -1  # Cannot find anything in an empty array
    assert search(nums, target) == expected, "Failed to return -1 for an empty array"

# Test case for a single-element array where the target is found
def test_search_single_element_found():
    nums = [1]
    target = 1
    expected = 0  # Target 1 is at index 0 in a single-element array
    assert search(nums, target) == expected, "Failed to find target in a single-element array"

# Test case for a single-element array where the target is not found
def test_search_single_element_not_found():
    nums = [2]
    target = 1
    expected = -1  # Target 1 is not in the single-element array
    assert search(nums, target) == expected, "Failed to return -1 for a single-element array when target is not found"
