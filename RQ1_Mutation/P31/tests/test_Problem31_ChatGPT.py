# test file
import pytest
from Problem31_GeneratedSolution import findOrder  # Adjust this import based on your file structure

# Test case with no prerequisites
def test_no_prerequisites():
    numCourses = 4
    prerequisites = []
    # Any order is valid; checking for length and uniqueness of courses
    result = findOrder(numCourses, prerequisites)
    assert len(result) == numCourses and len(set(result)) == numCourses, "Failed with no prerequisites"

# Test case with a simple linear order
def test_linear_order():
    numCourses = 3
    prerequisites = [[1, 0], [2, 1]]
    expected = [0, 1, 2]  # The only valid order
    assert findOrder(numCourses, prerequisites) == expected, "Failed with a simple linear order"

# Test case with a circular dependency
def test_circular_dependency():
    numCourses = 3
    prerequisites = [[1, 0], [2, 1], [0, 2]]
    expected = []  # No valid order due to circular dependency
    assert findOrder(numCourses, prerequisites) == expected, "Failed to identify circular dependency"

# Test case with complex dependencies
def test_complex_dependencies():
    numCourses = 6
    prerequisites = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
    # Multiple valid orders possible, checking for one of the valid solutions
    valid_solution_sets = [
        [0, 1, 3, 2, 4, 5],
        [1, 0, 3, 2, 4, 5]
    ]
    result = findOrder(numCourses, prerequisites)
    assert result in valid_solution_sets, "Failed with complex dependencies"

# Test case with self dependency (impossible to complete)
def test_self_dependency():
    numCourses = 2
    prerequisites = [[0, 0]]
    expected = []  # No valid order due to self dependency
    assert findOrder(numCourses, prerequisites) == expected, "Failed to identify self dependency"

# Test case for a large number of courses
def test_large_number_of_courses():
    numCourses = 1000
    prerequisites = [[i, i - 1] for i in range(1, 1000)]
    result = findOrder(numCourses, prerequisites)
    # Verifying the first and last courses in the expected linear order
    assert result[0] == 0 and result[-1] == 999, "Failed with a large number of courses"

# Test case with no possible order due to a partial cycle
def test_partial_cycle():
    numCourses = 4
    prerequisites = [[0, 1], [1, 2], [2, 0], [3, 2]]
    expected = []  # No valid order because of the cycle 0 -> 1 -> 2 -> 0
    assert findOrder(numCourses, prerequisites) == expected, "Failed to identify partial cycle"

