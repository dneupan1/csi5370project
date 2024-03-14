
def coinChange(coins, amount):
    """
    Find the fewest number of coins needed to make up a given amount.
    
    :param coins: List[int], the denominations of the coins available.
    :param amount: int, the total amount of money.
    :return: int, the fewest number of coins needed, or -1 if the amount cannot be made.
    """
    # Initialize DP array where dp[i] is the fewest number of coins making up amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make up amount 0
    
    # Fill the DP array
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Check if we found a solution for the given amount
    return dp[amount] if dp[amount] != float('inf') else -1


