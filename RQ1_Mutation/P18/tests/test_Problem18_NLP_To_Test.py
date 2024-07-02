import pytest
from Problem18_GeneratedSolution import flipLights  # Assuming the function 'flipLights' is defined in 'solution.py'

@pytest.mark.parametrize("n, presses, expected", [
    # Example 1: Single bulb with one press
    (1, 1, 2),
    # Example 2: Two bulbs with one press
    (2, 1, 3),
    # Example 3: Three bulbs with one press
    (3, 1, 4),
    # Edge case: No presses, all bulbs remain on
    (3, 0, 1),
    # Edge case: Single bulb with no presses
    (1, 0, 1),
    # Multiple presses with two bulbs
    (2, 2, 4),
    # Multiple presses with three bulbs
    (3, 2, 7),
    # Larger number of bulbs with multiple presses
    (4, 1, 4),
    (4, 2, 7),
    (5, 3, 8),
    # Large number of presses, should result in maximum unique patterns
    (4, 100, 8),
])
def test_flipLights(n, presses, expected):
    """
    Tests the flipLights function with various values of n and presses to ensure it correctly counts the number of different possible statuses of bulbs.

    This test function verifies:
    - Proper handling of different numbers of bulbs and presses.
    - Edge cases such as no presses and single bulb scenarios.
    - Correct counting of unique statuses with multiple presses.

    Args:
    n (int): The number of bulbs.
    presses (int): The number of button presses allowed.
    expected (int): The expected number of different possible statuses of the bulbs.
    """
    result = flipLights(n, presses)
    assert result == expected, f"Test failed for n={n}, presses={presses}. Expected {expected}, got {result}"
