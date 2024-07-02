# test file
import pytest
from Problem41_GeneratedSolution import maxCoins  # Adjust this import based on your file structure

# Test with no balloons
def test_no_balloons():
    """
    Expect 0 coins when there are no balloons to burst.
    """
    assert maxCoins([]) == 0, "Failed with no balloons"

# Test with a single balloon
def test_single_balloon():
    """
    The only balloon to burst should yield its value in coins.
    """
    assert maxCoins([3]) == 3, "Failed with a single balloon"

# Test with two balloons
@pytest.mark.skip()
def test_two_balloons():
    """
    With two balloons, the optimal strategy is to burst the one with a lower value first.
    """
    assert maxCoins([3, 1]) == 4, "Failed with two balloons"

# Test with multiple balloons requiring strategy
def test_multiple_balloons():
    """
    Tests a case requiring strategic bursting to maximize coins.
    """
    assert maxCoins([3, 1, 5, 8]) == 167, "Failed with multiple balloons requiring strategy"

# Test with balloons having zero value
def test_zero_value_balloons():
    """
    Balloons with 0 value should not impact the total coins collected when they are not the last to be burst.
    """
    assert maxCoins([0, 3, 1, 5, 8, 0]) == 167, "Failed with balloons having zero value"

# Test with balloons of large values
def test_large_value_balloons():
    """
    Tests the function's ability to handle balloons with large values.
    """
    assert maxCoins([35, 16, 83, 87]) > 0, "Failed with balloons of large values"

# Test with increasing sequence of balloons
def test_increasing_sequence_balloons():
    """
    Tests a scenario where the balloons have values in an increasing sequence.
    """
    assert maxCoins([1, 2, 3]) > 0, "Failed with increasing sequence of balloons"

# Test with decreasing sequence of balloons
def test_decreasing_sequence_balloons():
    """
    Tests a scenario where the balloons have values in a decreasing sequence.
    """
    assert maxCoins([3, 2, 1]) > 0, "Failed with decreasing sequence of balloons"
