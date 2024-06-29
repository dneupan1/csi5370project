def exist(board, word):
    """
    Determines if a given word exists in a grid by exploring sequentially adjacent cells.
    
    Args:
    board (List[List[str]]): A 2D grid of characters.
    word (str): The word to search for in the grid.
    
    Returns:
    bool: True if the word exists in the grid, otherwise False.
    
    Explanation:
    We use DFS to explore each cell as a potential starting point for the word. During the search,
    we mark cells as visited by temporarily changing their value and restore it after the recursion.
    """
    if not board or not word:
        return False

    rows, cols = len(board), len(board[0])
    
    def dfs(r, c, index):
        if index == len(word):
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]:
            return False

        # Mark the cell as visited
        temp, board[r][c] = board[r][c], '#'

        # Explore the four possible directions: up, down, left, right
        found = (dfs(r+1, c, index+1) or
                 dfs(r-1, c, index+1) or
                 dfs(r, c+1, index+1) or
                 dfs(r, c-1, index+1))

        # Restore the cell's original value
        board[r][c] = temp
        
        return found

    # Start from each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True

    return False