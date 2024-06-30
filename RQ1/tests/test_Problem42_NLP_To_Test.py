import pytest
from Problem42_GeneratedSolution import mergeStones as minimum_merge_cost  # Assuming the function is named 'minimum_merge_cost' and is in 'solution.py'

@pytest.mark.parametrize("stones, k, expected", [
    ([3, 2, 4, 1], 2, 20),  # Example 1 from the problem statement
    ([3, 2, 4, 1], 3, -1),  # Example 2 from the problem statement, impossible to finish merging
    ([3, 5, 1, 2, 6], 3, 25),  # Example 3 from the problem statement
    ([1, 2, 3, 4, 5, 6], 2, 68),  # Multiple merges required, generic case
    ([10], 1, 0),  # Single pile, no merge needed, should return 0 cost
    ([7, 9, 3, 4, 8, 2], 4, 66),  # Merging four piles at a time
    ([10, 20, 30], 4, -1),  # Fewer piles than k, impossible to merge
    ([5, 5, 5, 5], 2, 30),  # Equal size piles, two merges total
    ([50, 40, 30, 20, 10], 5, 150),  # All piles in one go
    ([4, 1, 2, 3, 9, 10], 3, 42)  # Complex scenario requiring strategic merges
])
def test_minimum_merge_cost(stones, k, expected):
    """
    Tests the minimum_merge_cost function with various configurations of stone piles and merge size 'k' to ensure it returns the minimum merging cost correctly.

    This function checks:
    - Correct computation of merging costs under constraints.
    - Ability to handle cases where merging all piles is not possible.
    - Validation against different pile configurations and values of k.

    Args:
    stones (list of int): List of stone counts in each pile.
    k (int): The number of consecutive piles that must be merged in each operation.
    expected (int): The expected minimum cost to merge all piles into one, or -1 if it's impossible.
    """
    assert minimum_merge_cost(stones, k) == expected, f"Test failed for stones={stones}, k={k}"
