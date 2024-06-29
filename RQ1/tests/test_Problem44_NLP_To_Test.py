from typing import List

def maxValueOfCoins(piles: List[List[int]], k: int) -> int:
    """
    This function returns the maximum total value of coins you can have in your wallet
    if you choose exactly k coins optimally from the given piles.
    
    :param piles: List[List[int]] - A list where each element is a list of integers representing a pile of coins
    :param k: int - The exact number of coins to choose
    :return: int - Maximum total value of coins
    """
    
    # Number of piles
    n = len(piles)
    
    # DP array to store maximum value of coins for choosing j coins from the first i piles
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Iterate over each pile
    for i in range(1, n + 1):
        # Iterate over the number of coins to choose
        for j in range(0, k + 1):
            # Initialize current sum of coins for the current pile
            current_sum = 0
            # Iterate over the coins in the current pile
            for x in range(0, min(len(piles[i-1]), j) + 1):
                if x > 0:
                    current_sum += piles[i-1][x-1]
                dp[i][j] = max(dp[i][j], dp[i-1][j-x] + current_sum)
    
    # Return the maximum value for choosing k coins from all piles
    return dp[n][k]