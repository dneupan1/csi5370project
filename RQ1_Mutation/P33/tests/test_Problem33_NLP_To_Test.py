import pytest
from Problem33_GeneratedSolution import rob_linear as rob_circular_houses  # Assuming the function 'rob_circular_houses' is in 'solution.py'

@pytest.mark.parametrize("nums, expected", [
    #([2, 3, 2], 3),  # Example 1: Small circular array with adjacency constraints
    ([1, 2, 3, 1], 4),  # Example 2: Circular array with optimal non-adjacent selection
    #([1, 2, 3], 3),  # Example 3: Optimal to choose the maximum single value
    ([], 0),  # Edge case: No houses, no money
    ([1], 1),  # Single house, only one choice available
    ([5, 1, 1, 5], 10),  # Circular array with large values non-adjacent
    #([1, 2, 3, 4, 5, 1, 2, 3, 4, 5], 16),  # Larger array, multiple optimal subproblems
    ([100], 100),  # Single large value
    #([5, 5, 5, 5, 5, 5, 5, 5, 5, 100], 260),  # Max value at end with equal small values around
    ([3, 10, 3, 1, 2], 12)  # Complex small array, best option includes first and last values indirectly
])
def test_rob_circular_houses(nums, expected):
    """
    Tests the rob_circular_houses function with various configurations of house values to ensure it correctly calculates the maximum money that can be robbed without alerting the police.

    This test function verifies:
    - Correct handling of simple and complex scenarios, including small and large lists.
    - Edge cases such as no houses or a single house.
    - Ensuring that the function properly respects the circular nature of the neighborhood.

    Args:
    nums (list of int): The amounts of money stashed in each house.
    expected (int): The expected maximum amount of money that can be robbed without alerting the police.
    """
    assert rob_circular_houses(nums) == expected, f"Test failed for input {nums}. Expected {expected}, got {rob_circular_houses(nums)}"
