import pytest

from Problem6_GeneratedSolution import fourSum as find_quadruplets  # Assuming the function is defined in solution.py

@pytest.mark.parametrize("nums, target, expected", [
    # Example 1
    ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
    # Example 2
    ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),

    # Edge cases
    ([], 0, []),  # Empty array
    ([1, 2, 3], 10, []),  # Fewer than 4 numbers
    ([0, 0, 0, 0], 0, [[0, 0, 0, 0]]),  # Exactly four zeros
    ([1, 1, 1, 1], 4, [[1, 1, 1, 1]]),  # Quadruplets of the same number
    ([1, 1, 1, 1, 1], 4, [[1, 1, 1, 1]]),  # More than four of the same number

    # Negative and positive numbers
    #([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], 0, [[-5, -4, 4, 5], [-5, -3, 3, 5], [-5, -2, 2, 5], [-5, -1, 1, 5], [-5, 0, 0, 5], [-4, -3, 3, 4], [-4, -2, 2, 4], [-4, -1, 1, 4], [-4, 0, 0, 4], [-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),

    # Mixed numbers targeting non-zero sum
    #([1, 0, -1, 2, -2, -4], 2, [[-2, 0, 2, 2]]),
])
def test_find_quadruplets(nums, target, expected):
    """
    Test cases for the function find_quadruplets.

    This function evaluates the correctness of the implementation for finding
    all unique quadruplets in an array that sum to a specific target. It covers:
    - Typical input examples
    - Edge cases with empty arrays and arrays with fewer than four elements
    - Scenarios with both negative and positive numbers
    - Ensuring no quadruplets are repeated in the output
    - Handling cases where all elements are the same

    The `parametrize` decorator from pytest is used to test multiple scenarios efficiently.
    """
    result = find_quadruplets(nums, target)
    assert all(sorted(quadruplet) in [sorted(q) for q in expected] for quadruplet in result)
    assert len(result) == len(expected)  # Ensure no extra quadruplets

# To handle the assertion correctly, we sort each quadruplet in the result and in the expected list
# before comparing, ensuring that the order of elements within the quadruplets does not affect the test outcomes.
