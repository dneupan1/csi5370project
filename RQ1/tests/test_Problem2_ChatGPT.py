import pytest
from Problem2_GeneratedSolution import count_good_subarrays  # Adjust the import path according to your project structure


@pytest.mark.parametrize("nums, k, expected", [
    ([1, 2, 1, 2, 3], 2, 7),  # Normal case with mixed numbers
    ([1, 2, 3, 4], 2, 3),  # Normal case with all unique numbers
    ([1, 1, 1, 1], 1, 10),  # Corrected: All elements are the same, use formula n*(n+1)/2 -> 4*5/2 = 10
    ([1, 2, 3, 4], 4, 1),  # Boundary case with k equal to number of unique elements
    ([1, 2, 2, 1], 1, 5),  # Normal case with repeating numbers
    ([], 1, 0),  # Edge case with an empty array
    ([1, 1], 1, 3),  # Corrected: Two identical elements, n*(n+1)/2 -> 2*3/2 = 3
    ([1, 1, 1], 1, 6),  # Corrected: Three identical elements, n*(n+1)/2 -> 3*4/2 = 6
])
def test_count_good_subarrays(nums, k, expected):
    """
    Tests the count_good_subarrays function with various inputs to ensure it correctly counts the number of
    good subarrays where the number of different integers is exactly k.
    
    Args:
        nums (List[int]): The input array of integers.
        k (int): The exact number of different integers in a good subarray.
        expected (int): The expected number of good subarrays, adjusted for arrays of identical elements.
    """
    assert count_good_subarrays(nums, k) == expected, f"Failed with nums={nums}, k={k}, expected={expected}"
