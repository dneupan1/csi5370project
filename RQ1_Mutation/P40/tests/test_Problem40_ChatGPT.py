# test file
import pytest
from Problem40_GeneratedSolution import NumArray  # Adjust this import based on your file structure

# Test initializing the NumArray with a typical array
def test_initialization():
    """
    Test to ensure the segment tree is correctly initialized with the given array.
    This does not directly test the internal structure but ensures the sumRange function
    works correctly immediately after initialization.
    """
    nums = [1, 3, 5]
    numArray = NumArray(nums)
    assert numArray.sumRange(0, 2) == sum(nums), "Failed to correctly initialize the segment tree"

# Test updating a single element and querying a range
def test_update_and_query():
    """
    Test updating a single element in the array and then querying a range to ensure the update
    is reflected in the range sum.
    """
    nums = [1, 3, 5]
    numArray = NumArray(nums)
    numArray.update(1, 2)  # Update index 1 from 3 to 2
    assert numArray.sumRange(0, 2) == 8, "Failed to reflect update in the range sum"

# Test querying the sum of the entire array
def test_sum_entire_array():
    """
    Tests querying the sum of the entire array to ensure the segment tree covers the full array.
    """
    nums = [1, 3, 5, 7, 9]
    numArray = NumArray(nums)
    assert numArray.sumRange(0, len(nums) - 1) == sum(nums), "Failed to sum the entire array correctly"

# Test querying a sub-range
def test_subrange_query():
    """
    Tests querying a sub-range of the array to ensure intermediate nodes in the segment tree
    correctly represent the sums of their corresponding sub-arrays.
    """
    nums = [1, 3, 5, 7, 9]
    numArray = NumArray(nums)
    assert numArray.sumRange(1, 3) == sum(nums[1:4]), "Failed to query a sub-range correctly"

# Test updating the first and last elements
def test_update_edges():
    """
    Tests updating the first and last elements in the array to ensure the segment tree
    correctly handles updates at the edges of the array.
    """
    nums = [1, 3, 5, 7, 9]
    numArray = NumArray(nums)
    numArray.update(0, 10)  # Update the first element
    numArray.update(len(nums) - 1, 20)  # Update the last element
    assert numArray.sumRange(0, len(nums) - 1) == 10 + sum(nums[1:-1]) + 20, "Failed to update the edges correctly"

# Edge case: Test with a single-element array
def test_single_element():
    """
    Tests initializing, updating, and querying a NumArray with a single element,
    to ensure the segment tree correctly handles arrays of size one.
    """
    nums = [10]
    numArray = NumArray(nums)
    numArray.update(0, 5)
    assert numArray.sumRange(0, 0) == 5, "Failed with a single-element array"
