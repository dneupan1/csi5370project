from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    """
    This function returns the fewest number of coins needed to make up the given amount.
    If the amount cannot be made up by any combination of the coins, it returns -1.
    
    :param coins: List[int] - List of coin denominations
    :param amount: int - Total amount of money
    :return: int - Fewest number of coins needed or -1 if not possible
    """
    
    # Create a list to store the minimum number of coins needed for each amount up to the given amount
    # Initialize the list with a value higher than the possible number of coins, here amount + 1
    dp = [amount + 1] * (amount + 1)
    
    # Base case: The minimum number of coins needed to make amount 0 is 0
    dp[0] = 0
    
    # Loop through each amount from 1 to the given amount
    for a in range(1, amount + 1):
        # Loop through each coin in the coin list
        for coin in coins:
            if a - coin >= 0:  # Check if the coin can contribute to the current amount
                dp[a] = min(dp[a], dp[a - coin] + 1)  # Choose the minimum coins needed
    
    # If dp[amount] is still greater than amount, it means we cannot make the amount with the given coins
    return dp[amount] if dp[amount] != amount + 1 else -1