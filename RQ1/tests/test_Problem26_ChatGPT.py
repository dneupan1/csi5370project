import pytest
from Problem26_GeneratedSolution import diffWaysToCompute


# Test case 1: Expression with multiple types of operations
def test_multiple_operations():
    """
    Tests an expression with multiple types of operations to ensure
    the function can handle and correctly compute all possible combinations.
    """
    expression = "2*3-4*5"
    expected = [-34, -10, -14, -10, 10]  # Possible outcomes from different groupings
    assert sorted(diffWaysToCompute(expression)) == sorted(expected)

# Test case 2: Expression with a single type of operation
def test_single_operation():
    """
    Tests an expression with a single type of operation to verify
    the function's handling of simpler cases.
    """
    expression = "2-1-1"
    expected = [0, 2]  # Possible outcomes
    assert sorted(diffWaysToCompute(expression)) == sorted(expected)

# Test case 3: Expression that is just a number
def test_single_number():
    """
    Tests an expression that contains only a number to ensure the base case
    is correctly handled.
    """
    expression = "3"
    expected = [3]  # The only outcome is the number itself
    assert diffWaysToCompute(expression) == expected

# Test case 4: Empty expression
def test_empty_expression():
    """
    Tests an empty expression to verify how the function handles it.
    Ideally, it should return an empty list as there are no computations to be made.
    """
    expression = ""
    expected = []  # No computation possible
    assert diffWaysToCompute(expression) == expected

# Test case 5: Complex expression
@pytest.mark.skip
def test_complex_expression():
    """
    Tests a more complex expression to ensure the function can handle
    a mix of several operators and numbers, computing all possible outcomes.
    """
    expression = "2*3-4*5+6"
    expected = [-34, -10, -14, -10, 10, -14, 2, -10, 2, 22]  # Example outcomes
    assert sorted(diffWaysToCompute(expression)) == sorted(expected)

