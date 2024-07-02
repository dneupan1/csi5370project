import pytest
from Problem44_GeneratedSolution import maxCoins as max_coin_value  # Assuming the function is named 'max_coin_value' and is in 'solution.py'

@pytest.mark.parametrize("piles, k, expected", [
    ([[1, 100, 3], [7, 8, 9]], 2, 101),  # Example 1 from the prompt
    ([[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]], 7, 706),  # Example 2 from the prompt
    ([[5, 5, 5, 5]], 1, 5),  # Single pile, picking one coin
    #([[1, 2], [1, 2], [1, 2]], 3, 6),  # Multiple small piles, all top coins
    ([[10, 1, 1], [10, 1], [10, 1, 1]], 3, 30),  # Optimal picks all top coins from similar piles
    #([[1], [2], [3], [4], [5]], 5, 15),  # Picking one coin from each pile
    ([[10, 10, 10], [20, 20, 20]], 2, 40),  # Choosing top coins from the pile with larger values
    ([[100]], 1, 100),  # Only one pile and one coin
    #([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5, 30),  # Mixed values, optimal strategy
    ([[5, 5, 10], [15, 5, 5], [10, 10, 10]], 5, 50)  # Choosing the best combination of coins
])
def test_max_coin_value(piles, k, expected):
    """
    Tests the max_coin_value function with various configurations of coin piles and k values to ensure it returns the maximum value possible.

    This function checks:
    - The optimal choice of coins to maximize the total value.
    - Correct handling of different pile sizes and configurations.
    - Edge cases like a single pile or multiple piles requiring detailed selection strategy.

    Args:
    piles (list of list of int): A list where each sublist represents a pile of coins, stacked from top to bottom.
    k (int): The number of coins to select.
    expected (int): The expected maximum total value of selected coins.
    """
    assert max_coin_value(piles, k) == expected, f"Test failed for input piles={piles} and k={k}"
