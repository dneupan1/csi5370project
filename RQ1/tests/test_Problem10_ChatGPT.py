import pytest
from Problem10_GeneratedSolution import cherryPickup  # Adjust the import path as needed

def test_no_path():
    """
    Test grid where no path exists to reach the end.
    """
    grid = [
        [1, -1],
        [-1, 1]
    ]
    expected = 0  # No cherries can be picked since there's no path to the end.
    assert cherryPickup(grid) == expected, "Failed to handle grid with no valid path."
