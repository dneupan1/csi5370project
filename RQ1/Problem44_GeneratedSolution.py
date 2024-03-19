
def maxCoins(piles, k):
    """
    Find the maximum total value of coins by choosing exactly k coins from the given piles.
    
    :param piles: List[List[int]], the composition of each pile from top to bottom.
    :param k: int, the total number of coins to choose.
    :return: int, the maximum total value of coins.
    """
    # Preprocess each pile to have cumulative sums for easy computation of coin sums
    for i in range(len(piles)):
        for j in range(1, len(piles[i])):
            piles[i][j] += piles[i][j - 1]
    
    # Initialize a dp table where dp[i][j] represents the maximum value for choosing j coins from the first i piles
    dp = [[0] * (k + 1) for _ in range(len(piles) + 1)]
    
    # Fill dp table
    for i in range(1, len(piles) + 1):
        for j in range(1, k + 1):
            # Calculate dp[i][j] considering all possible number of coins taken from the ith pile
            for x in range(min(j, len(piles[i-1])) + 1):
                dp[i][j] = max(dp[i][j], (piles[i-1][x-1] if x > 0 else 0) + dp[i-1][j-x])
    
    # The answer is the maximum value for choosing k coins from all piles
    return dp[len(piles)][k]

