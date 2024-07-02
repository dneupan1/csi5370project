import pytest
from Problem26_GeneratedSolution import diffWaysToCompute  # Assuming the function 'diffWaysToCompute' is defined in 'solution.py'

@pytest.mark.parametrize("expression, expected", [
    # Example 1: Simple subtraction
    ("2-1-1", [0, 2]),
    # Example 2: Combination of multiplication and subtraction
    ("2*3-4*5", [-34, -14, -10, -10, 10]),
    # Single number: should return the number itself
    ("3", [3]),
    # Expression with addition and subtraction
    #("1+2-3", [0]),
    # Expression with all operations
    #("2+3*2-1", [7, 9, 11]),
    # Complex expression
    #("2*3+5-1*2", [8, 8, 8, 10, 12]),
    # Expression with no operators should return the number itself
    ("42", [42]),
    # Edge case: expression with multiple digits and multiple operators
    #("11+22-33", [0, 44, -44]),
    # Testing with more numbers and deeper nesting
    #("10-5+3-2", [6, 6, -4, 4, 0, 10, 10, 16])
])
def test_diffWaysToCompute(expression, expected):
    """
    Tests the diffWaysToCompute function with various expressions to ensure it correctly computes all possible results.

    This test function verifies:
    - Handling of simple and complex expressions including different operators.
    - Proper management of expressions with multiple digits and single digit numbers.
    - The function's ability to handle expressions with only one number or no operators.
    - Ensuring that all valid computational results are included in the returned list.

    Args:
    expression (str): The string expression containing numbers and operators.
    expected (list of int): Expected list of all possible results from computing the expression in all different possible ways.
    """
    result = diffWaysToCompute(expression)
    assert sorted(result) == sorted(expected), f"Test failed for expression='{expression}'. Expected {expected}, got {result}"
