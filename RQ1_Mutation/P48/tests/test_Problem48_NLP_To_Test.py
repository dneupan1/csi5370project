import pytest
from Problem48_GeneratedSolution import maxProduct as max_product  # Assuming the function to be tested is named 'max_product' and is in 'solution.py'

@pytest.mark.parametrize("n, expected", [
    (2, 1),  # Minimal case with smallest n
    (10, 36),  # Example case from the prompt with a known solution
    (3, 2),  # Case where n is 3, which should split into 1 and 2
    (4, 4),  # Case where n is 4, optimal split is 2 and 2
    (5, 6),  # Case where n is 5, optimal split is 2 and 3
    (6, 9),  # Case where n is 6, optimal split is 3 and 3
    (8, 18),  # Tests n value where breaking into parts of 3 and the remainder yields maximum product
    (11, 54),  # Similar to the above but with higher n to check consistency
    (15, 243),  # Larger n to see how the function performs with more numbers
    (20, 1458)  # Another large n to test robustness and scaling of the algorithm
])
def test_max_product(n, expected):
    """
    Test the max_product function with various values of n to ensure it correctly calculates the maximum product.

    This function tests a range of inputs from the smallest possible value (n=2) to larger values (up to n=20) to ensure the algorithm correctly handles and scales for different inputs. The chosen values include:
    - Edge cases with smallest values
    - Known solutions for moderate values
    - Progressive scaling to test algorithmic performance and correctness under increasing problem sizes.

    Args:
    n (int): The integer to be broken down into the sum of at least two positive integers.
    expected (int): The expected maximum product of those integers.
    """
    assert max_product(n) == expected, f"Failed on input {n}"
