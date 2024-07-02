import pytest
from Problem50_GeneratedSolution import canCross as can_cross  # Assuming the function to be tested is named 'can_cross' and is in 'solution.py'

@pytest.mark.parametrize("stones, expected", [
    ([0, 1, 3, 5, 6, 8, 12, 17], True),
    ([0, 1, 2, 3, 4, 8, 9, 11], False),
    ([0, 1, 3, 6, 10], True),  # Additional test case: increasing jump lengths exactly matching stone positions
    ([0, 2], False),  # Test case where the frog cannot make the first jump
    #([0, 1, 3, 7, 14], True)  # Test case with maximum allowable jumps
])
def test_can_cross(stones, expected):
    """
    Test the can_cross function with various lists of stones and their expected outcomes.

    Each test case checks whether the frog can reach the last stone based on the given stone positions.
    The test inputs vary to cover different scenarios including possible jumps, no possible jumps, and exactly matching jumps.

    Args:
    stones (list of int): The positions of stones in the river.
    expected (bool): The expected result indicating whether the frog can reach the last stone or not.
    """
    assert can_cross(stones) == expected, f"Failed on input {stones}"
