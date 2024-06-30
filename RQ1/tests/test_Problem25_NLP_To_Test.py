import pytest
from Problem25_GeneratedSolution import addOperators  # Assuming the function 'addOperators' is defined in 'solution.py'

@pytest.mark.parametrize("num, target, expected", [
    # Example 1: Simple case with multiple solutions
    ("123", 6, ["1+2+3", "1*2*3"]),
    # Example 2: Simple case with different operator precedence
    ("232", 8, ["2*3+2", "2+3*2"]),
    # Example 3: Large number with no possible solution
    ("3456237490", 9191, []),
    # Single digit with target equals to number
    ("5", 5, ["5"]),
    # Single digit with target not equals to number
    ("5", 3, []),
    # Case where only subtraction or addition can work
    ("105", 5, ["1*0+5", "10-5"]),
    # Long number with possible multiple solutions
    ("12345", 15, ["1*2+3*4+5", "12+3-45+55"]),
    # Zeroes in the number
    ("000", 0, ["0*0*0", "0+0+0", "0-0+0"]),
    # Multiple zeroes with non-zero target
    ("000", 1, []),
    # Operators must not generate operands with leading zeros
    ("10203", 6, ["10+2-3*2", "1*0+2*3+0*3"]),
])
def test_addOperators(num, target, expected):
    """
    Tests the addOperators function with various numbers and targets to ensure it correctly computes all valid expressions that evaluate to the target.

    This test function checks:
    - The function's ability to generate valid arithmetic expressions that correctly evaluate to the target using the digits of the number.
    - Proper handling of edge cases, such as numbers containing zeroes, leading zeroes in operands, and single-digit numbers.
    - The correctness of expressions with varying lengths of input numbers.
    
    Args:
    num (str): The string of digits.
    target (int): The target integer value.
    expected (list of str): A list of strings containing valid expressions or an empty list if no valid expressions exist.
    """
    result = addOperators(num, target)
    assert sorted(result) == sorted(expected), f"Test failed for num='{num}', target={target}. Expected {expected}, got {result}"
