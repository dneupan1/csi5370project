def minPathSum(grid: list[list[int]]) -> int:
    """
    This function finds the path from top left to bottom right in a grid that minimizes the sum of all numbers along its path.
    You can only move either down or right at any point in time.
    
    :param grid: 2D list of non-negative numbers
    :return: Minimum sum of all numbers along the path
    """
    
    # Number of rows and columns in the grid
    m, n = len(grid), len(grid[0])
    
    # Create a 2D DP array to store the minimum path sums
    dp = [[0] * n for _ in range(m)]
    
    # Initialize the DP array with the value at the start position
    dp[0][0] = grid[0][0]
    
    # Fill the first row of the DP array
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    
    # Fill the first column of the DP array
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    
    # Fill the rest of the DP array
    for i in range(1, m):
        for j in range(1, n):
            # The cell dp[i][j] can be reached either from dp[i-1][j] or dp[i][j-1]
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    
    # The value at dp[m-1][n-1] is the minimum path sum to reach the bottom-right corner
    return dp[m - 1][n - 1]