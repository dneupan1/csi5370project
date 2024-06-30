import pytest
from Problem16_GeneratedSolution import reconstructQueue  # Assuming the function 'reconstructQueue' is defined in 'solution.py'

@pytest.mark.parametrize("people, expected", [
    # Example 1: Provided example
    ([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]], [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]),
    # Example 2: Provided example
    ([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]], [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]]),
    # Single person
    ([[5, 0]], [[5, 0]]),
    # Two people with the same height and different k values
    ([[7, 0], [7, 1]], [[7, 0], [7, 1]]),
    # All people have height 1
    ([[1, 0], [1, 1], [1, 2], [1, 3]], [[1, 0], [1, 1], [1, 2], [1, 3]]),
    # People in descending order of height
    ([[7, 0], [6, 0], [5, 0], [4, 0]], [[4, 0], [5, 0], [6, 0], [7, 0]]),
    # People with no one taller in front
    ([[5, 0], [6, 0], [7, 0]], [[5, 0], [6, 0], [7, 0]]),
    # Random heights and k values
    ([[3, 1], [4, 2], [2, 0], [1, 3]], [[2, 0], [3, 1], [4, 2], [1, 3]]),
    # Edge case: Multiple people with k equal to their index
    ([[4, 0], [5, 1], [6, 2], [7, 3]], [[4, 0], [5, 1], [6, 2], [7, 3]])
])
def test_reconstructQueue(people, expected):
    """
    Tests the reconstructQueue function with various inputs to ensure it correctly reconstructs the queue based on the given attributes.

    This test function verifies:
    - Handling of provided examples and basic functionality.
    - Proper handling of edge cases such as single person, multiple people with same height, and people in descending order of height.
    - Correct reconstruction for random heights and `k` values.

    Args:
    people (list of list of int): The input list of people with [height, k] attributes.
    expected (list of list of int): The expected output list representing the reconstructed queue.
    """
    result = reconstructQueue(people)
    assert result == expected, f"Test failed for people={people}. Expected {expected}, got {result}"
