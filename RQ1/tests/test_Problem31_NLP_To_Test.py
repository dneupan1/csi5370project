import pytest
from Problem31_GeneratedSolution import findOrder as find_course_order  # Assuming the function is named 'find_course_order' and is in 'solution.py'

@pytest.mark.parametrize("numCourses, prerequisites, expected", [
    # Example 1: Linear dependency
    (2, [[1, 0]], [0, 1]),
    # Example 2: Complex dependencies with multiple valid solutions
    (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [[0, 1, 2, 3], [0, 2, 1, 3]]),
    # Example 3: No prerequisites
    (1, [], [0]),
    # Multiple valid orders with no prerequisites
    (3, [], [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]),
    # Circular dependency, should return empty
    (3, [[0, 1], [1, 2], [2, 0]], []),
    # Partially connected graph with one course having no prerequisites
    (5, [[1, 0], [2, 1], [3, 2], [4, 1]], [[0, 1, 2, 3, 4], [0, 1, 4, 2, 3]]),
    # All courses are interconnected
    (3, [[0, 1], [1, 2], [2, 0]], []),
    # Single course with self-loop, impossible scenario
    (1, [[0, 0]], []),
    # Test large number of courses with simple chain
    (10, [[i, i - 1] for i in range(1, 10)], [i for i in range(10)])
])
def test_find_course_order(numCourses, prerequisites, expected):
    """
    Tests the find_course_order function with varying numbers of courses and prerequisite conditions to ensure it correctly computes a valid course order or identifies an impossible situation.

    This test function checks:
    - Handling of different graph structures including linear chains, complex graphs with multiple valid topological sorts, and graphs with circular dependencies.
    - Cases with no prerequisites to verify handling of simple scenarios.
    - Scenarios where a course order is impossible due to circular dependencies or self-loops.

    Args:
    numCourses (int): Number of courses.
    prerequisites (list of list of int): List where each element is a pair [a, b] indicating course a requires course b as a prerequisite.
    expected (list of list of int or empty list): Expected valid course orders or an empty list if no order is possible.
    """
    result = find_course_order(numCourses, prerequisites)
    if isinstance(expected[0], list):  # Multiple valid outputs possible
        assert result in expected, f"Test failed for numCourses={numCourses}, prerequisites={prerequisites}. Expected one of {expected}, got {result}"
    else:
        assert result == expected, f"Test failed for numCourses={numCourses}, prerequisites={prerequisites}. Expected {expected}, got {result}"
