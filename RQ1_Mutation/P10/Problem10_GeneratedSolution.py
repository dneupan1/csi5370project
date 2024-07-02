def cherryPickup(grid):
    n = len(grid)
    dp = [[[-1] * n for _ in range(n)] for _ in range(n)]
    
    def dfs(x1, y1, x2):
        y2 = x1 + y1 - x2
        # Base cases
        if x1 == n or y1 == n or x2 == n or y2 == n or grid[x1][y1] == -1 or grid[x2][y2] == -1:
            return -float('inf')  # Impossible path
        if dp[x1][y1][x2] != -1:
            return dp[x1][y1][x2]  # Memoization
        if x1 == n-1 and y1 == n-1:
            return grid[x1][y1]  # Reached the end
        
        # Recurrence relation
        cherries = grid[x1][y1]
        if x1 != x2:  # Avoid double-counting
            cherries += grid[x2][y2]
        dp[x1][y1][x2] = cherries + max(
            dfs(x1 + 1, y1, x2 + 1),  # Down-Down
            dfs(x1, y1 + 1, x2),      # Right-Down
            dfs(x1 + 1, y1, x2),      # Down-Right
            dfs(x1, y1 + 1, x2 + 1)   # Right-Right
        )
        
        return dp[x1][y1][x2]
    
    # Start the DFS from (0, 0, 0)
    result = dfs(0, 0, 0)
    return max(result, 0)  # Return 0 if no path is found
