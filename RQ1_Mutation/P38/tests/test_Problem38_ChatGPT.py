# test file
import pytest
from Problem38_GeneratedSolution import lengthOfLIS  # Adjust this import based on your file structure

# Test with an empty list
def test_empty_list():
    """
    An empty list has no subsequence, hence the length of the longest increasing
    subsequence should be 0.
    """
    assert lengthOfLIS([]) == 0, "Failed to return 0 for an empty list"

# Test with all elements being the same
def test_all_elements_same():
    """
    When all elements in the list are the same, the longest increasing subsequence
    can only be of length 1, as all elements are equal and there's no increase.
    """
    assert lengthOfLIS([5, 5, 5, 5]) == 1, "Failed with all elements the same"

# Test with a strictly increasing sequence
def test_strictly_increasing_sequence():
    """
    In a strictly increasing sequence, the entire list itself is the longest
    increasing subsequence. Thus, the expected result is the length of the list.
    """
    assert lengthOfLIS([1, 2, 3, 4, 5]) == 5, "Failed with a strictly increasing sequence"

# Test with a strictly decreasing sequence
def test_strictly_decreasing_sequence():
    """
    For a strictly decreasing sequence, the longest increasing subsequence has
    a length of 1, as no two elements can form an increasing sequence.
    """
    assert lengthOfLIS([5, 4, 3, 2, 1]) == 1, "Failed with a strictly decreasing sequence"

# Test with a mixed sequence
def test_mixed_sequence():
    """
    A mixed sequence that includes both increasing and decreasing elements.
    The test verifies the function's ability to identify the longest increasing
    subsequence within a complex sequence.
    """
    assert lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4, "Failed with a mixed sequence"

# Test with a single element
def test_single_element():
    """
    A list with a single element has a longest increasing subsequence of length 1,
    as the single element itself forms a valid increasing subsequence.
    """
    assert lengthOfLIS([1]) == 1, "Failed with a single element"

# Test with repeated elements contributing to LIS
def test_repeated_elements_contributing():
    """
    Tests a scenario where the list contains repeated elements that contribute
    to the length of the longest increasing subsequence.
    """
    assert lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6, "Failed with repeated elements contributing to LIS"
