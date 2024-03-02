import pytest
from Problem17_GeneratedSolution import countSmaller  # Adjust the import according to your project structure.

# Test case 1: Testing with a standard list of numbers
def test_standard_list():
    """
    Tests a standard list of numbers to verify if the function correctly counts
    the number of smaller elements to the right for each element.
    """
    nums = [5, 2, 6, 1]
    expected_counts = [2, 1, 1, 0]
    assert countSmaller(nums) == expected_counts

# Test case 2: Testing with a list in descending order
def test_descending_order():
    """
    Tests a list that is in descending order, which should result in counts
    incrementing from 0 up to n-1, where n is the list's length.
    """
    nums = [4, 3, 2, 1]
    expected_counts = [3, 2, 1, 0]
    assert countSmaller(nums) == expected_counts

# Test case 3: Testing with a list in ascending order
def test_ascending_order():
    """
    Tests a list in ascending order, where each element should have a count of 0
    because there are no smaller elements to the right.
    """
    nums = [1, 2, 3, 4]
    expected_counts = [0, 0, 0, 0]
    assert countSmaller(nums) == expected_counts

# Test case 4: Testing with an empty list
def test_empty_list():
    """
    Tests the function with an empty list to ensure it handles edge cases
    correctly and returns an empty list as expected.
    """
    nums = []
    expected_counts = []
    assert countSmaller(nums) == expected_counts

# Test case 5: Testing with a list of identical elements
def test_identical_elements():
    """
    Tests a list where all elements are identical, which should result in all
    counts being 0, as no element is smaller than any other.
    """
    nums = [5, 5, 5, 5]
    expected_counts = [0, 0, 0, 0]
    assert countSmaller(nums) == expected_counts

# Test case 6: Testing with a single element
def test_single_element():
    """
    Tests the function with a single-element list to verify that it correctly
    returns a count of 0, as there are no other elements to compare.
    """
    nums = [1]
    expected_counts = [0]
    assert countSmaller(nums) == expected_counts
