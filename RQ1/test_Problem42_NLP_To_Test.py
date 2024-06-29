def mergeStones(stones, k):
    """
    Returns the minimum cost to merge all piles of stones into one pile.
    If it is impossible, returns -1.
    
    Args:
    stones (List[int]): A list of integers representing the number of stones in each pile.
    k (int): The number of consecutive piles to merge in one move.
    
    Returns:
    int: The minimum cost to merge all piles into one pile, or -1 if impossible.
    """
    n = len(stones)
    
    # Check if it is possible to merge all piles into one
    if (n - 1) % (k - 1) != 0:
        return -1
    
    # Prefix sum array to calculate subarray sums efficiently
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + stones[i]
    
    # Initialize the DP table
    dp = [[[float('inf')] * (k + 1) for _ in range(n)] for _ in range(n)]
    
    # Base case: the cost to merge one pile into one pile is 0
    for i in range(n):
        dp[i][i][1] = 0
    
    # Fill the DP table
    for length in range(2, n + 1):  # Length of the subarray
        for i in range(n - length + 1):
            j = i + length - 1
            for m in range(2, k + 1):  # Number of piles
                for p in range(i, j, k - 1):
                    dp[i][j][m] = min(dp[i][j][m], dp[i][p][1] + dp[p + 1][j][m - 1])
            dp[i][j][1] = dp[i][j][k] + prefix_sum[j + 1] - prefix_sum[i] if dp[i][j][k] != float('inf') else float('inf')
    
    return dp[0][n - 1][1]