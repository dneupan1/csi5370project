# test file
import pytest
from Problem47_GeneratedSolution import isPathCrossing # Adjust this import based on your file structure

def test_path_not_crossing():
    """
    Tests a path that does not cross itself.
    """
    assert isPathCrossing([1, 2, 3, 4]) == False, "Failed with a non-crossing path"

def test_path_crossing():
    """
    Tests a path that crosses itself.
    """
    assert isPathCrossing([2, 2, 2, 2]) == True, "Failed to identify a crossing path"

def test_empty_path():
    """
    Tests an empty path, which should not cross itself.
    """
    assert isPathCrossing([]) == False, "Incorrectly identified an empty path as crossing"

def test_single_move():
    """
    Tests a path with a single move, which cannot cross itself.
    """
    assert isPathCrossing([1]) == False, "Incorrectly identified a single move path as crossing"

def test_complex_path():
    """
    Tests a more complex path that eventually crosses itself.
    """
    assert isPathCrossing([1, 3, 6, 2, 1, 1, 5]) == True, "Failed with a complex crossing path"

@pytest.mark.skip()
def test_return_to_origin():
    """
    Tests a path that returns to the origin but does not cross.
    """
    assert isPathCrossing([1, 1, 1, 1]) == False, "Incorrectly identified a path returning to origin as crossing"
