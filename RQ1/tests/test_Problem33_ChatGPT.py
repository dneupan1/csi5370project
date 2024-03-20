# test file
import pytest
from Problem33_GeneratedSolution import rob, rob_linear  # Adjust this import based on your file structure

# Tests for rob_linear
def test_rob_linear_empty():
    # Test handling of an empty list
    assert rob_linear([]) == 0, "Failed to handle empty list"

def test_rob_linear_single_house():
    # Test handling of a single house
    assert rob_linear([100]) == 100, "Failed with single house"

def test_rob_linear_two_houses():
    # Test handling of two houses
    assert rob_linear([100, 200]) == 200, "Failed with two houses"

def test_rob_linear_simple():
    # Test handling of a simple case
    assert rob_linear([1, 2, 3, 1]) == 4, "Failed with simple linear case"

def test_rob_linear_complex():
    # Test handling of a more complex case
    assert rob_linear([2, 7, 9, 3, 1]) == 12, "Failed with complex linear case"

# Tests for rob (circular houses)
def test_rob_single_house():
    # Test handling of a single house
    assert rob([100]) == 100, "Failed with single house in circular case"

def test_rob_two_houses():
    # Test handling of two houses
    assert rob([100, 200]) == 200, "Failed with two houses in circular case"

def test_rob_simple():
    # Test handling of a simple circular case
    assert rob([2, 3, 2]) == 3, "Failed with simple circular case"

def test_rob_complex():
    # Test handling of a more complex circular case
    assert rob([1, 2, 3, 1]) == 4, "Failed with complex circular case"

