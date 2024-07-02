
def minPathSum(grid):
    # Step 1: Initialize variables
    m, n = len(grid), len(grid[0])  # Dimensions of the grid
    
    # Step 2: Fill the first row and column
    # Fill the first column
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    # Fill the first row
    for j in range(1, n):
        grid[0][j] += grid[0][j-1]
    
    # Step 3: Fill the rest of the grid
    for i in range(1, m):
        for j in range(1, n):
            # Update the cell with the sum of itself and the min of the top or left cells
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    
    # Step 4: Return the value in the bottom-right cell
    return grid[-1][-1]
