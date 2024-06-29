def cherryPickup(grid: list[list[int]]) -> int:
    """
    This function returns the maximum number of cherries that can be collected
    by starting from (0,0) to (n-1,n-1) and back to (0,0) while picking up cherries.

    :param grid: 2D list representing the grid with cherries and thorns
    :return: Maximum number of cherries that can be collected
    """
    n = len(grid)
    
    # Memoization cache
    memo = {}

    def dp(r1, c1, r2, c2):
        """
        Helper function to calculate the maximum cherries that can be collected
        starting from (r1,c1) and (r2,c2) simultaneously.
        :param r1: Row of the first traversal
        :param c1: Column of the first traversal
        :param r2: Row of the second traversal
        :param c2: Column of the second traversal
        :return: Maximum number of cherries collected
        """
        # If out of bounds or on a thorn
        if r1 >= n or c1 >= n or r2 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
            return -float('inf')
        
        # If reached the end
        if r1 == n - 1 and c1 == n - 1:
            return grid[r1][c1]
        
        # Check if already computed
        if (r1, c1, r2, c2) in memo:
            return memo[(r1, c1, r2, c2)]
        
        # Collect cherries from the current positions
        cherries = grid[r1][c1]
        if r1 != r2 or c1 != c2:
            cherries += grid[r2][c2]

        # Explore the next steps (right and down)
        cherries += max(dp(r1 + 1, c1, r2 + 1, c2),  # both down
                        dp(r1 + 1, c1, r2, c2 + 1),  # first down, second right
                        dp(r1, c1 + 1, r2 + 1, c2),  # first right, second down
                        dp(r1, c1 + 1, r2, c2 + 1))  # both right

        # Memoize and return the result
        memo[(r1, c1, r2, c2)] = cherries
        return cherries

    # Initialize the process
    result = dp(0, 0, 0, 0)
    
    # If result is negative infinity, it means no valid path was found
    return max(0, result)