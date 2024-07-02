import pytest
from Problem18_GeneratedSolution import flipLights  # Adjust this import based on your project structure.

# Test case 1: No bulbs
def test_no_bulbs():
    """
    Tests the scenario where there are no bulbs. Regardless of the number of presses,
    the function should return 1, indicating a single configuration (all off).
    """
    assert flipLights(0, 5) == 1

# Test case 2: No presses
def test_no_presses():
    """
    Tests the scenario where no presses are made. Regardless of the number of bulbs,
    the function should return 1, indicating a single configuration (initial state).
    """
    assert flipLights(3, 0) == 1

# Test case 3: One bulb
def test_one_bulb():
    """
    Tests the scenario with a single bulb. Regardless of the number of presses,
    there should only be two possible configurations: on and off.
    """
    assert flipLights(1, 3) == 2

# Test case 4: Two bulbs, one press
def test_two_bulbs_one_press():
    """
    Tests two bulbs with a single press, which should result in three possible configurations.
    """
    assert flipLights(2, 1) == 3

# Test case 5: Two bulbs, multiple presses
def test_two_bulbs_multiple_presses():
    """
    Tests two bulbs with multiple presses, which should result in four possible configurations.
    """
    assert flipLights(2, 2) == 4

# Test case 6: Three bulbs, one press
def test_three_bulbs_one_press():
    """
    Tests three bulbs with a single press, which should result in four possible configurations.
    """
    assert flipLights(3, 1) == 4

# Test case 7: Three bulbs, two presses
def test_three_bulbs_two_presses():
    """
    Tests three bulbs with two presses, which should result in seven possible configurations.
    """
    assert flipLights(3, 2) == 7

# Test case 8: Three or more bulbs, three or more presses
def test_more_bulbs_more_presses():
    """
    Tests scenarios with three or more bulbs and three or more presses, which should always result in eight possible configurations.
    """
    assert flipLights(3, 3) == 8
    assert flipLights(5, 4) == 8  # Additional case to ensure coverage for more than three bulbs

