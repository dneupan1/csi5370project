


def exist(board, word):
    """
    Check if the word exists in the grid using Depth-First Search (DFS).
    
    The algorithm iterates through each cell in the grid. If a cell contains the first letter
    of the word, it initiates a DFS from that cell to search for the entire word in
    adjacent cells (up, down, left, right), ensuring not to use the same cell more than once
    in the same search path.
    
    :param board: List[List[str]], the grid of characters.
    :param word: str, the word to be searched in the grid.
    :return: bool, True if the word exists in the grid, False otherwise.
    """
    
    def dfs(index, x, y):
        """
        Perform DFS to search for the word in the grid starting from cell (x, y).
        
        :param index: int, current index in the word being searched.
        :param x: int, the row index in the grid.
        :param y: int, the column index in the grid.
        :return: bool, True if the rest of the word is found from this cell, False otherwise.
        """
        if index == len(word):
            # Entire word has been found
            return True
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[index]:
            # Out of bounds or current cell does not match the letter at index
            return False
        
        # Temporarily mark the cell as visited
        temp, board[x][y] = board[x][y], "#"
        
        # Explore all four directions
        found = (dfs(index + 1, x + 1, y) or
                 dfs(index + 1, x - 1, y) or
                 dfs(index + 1, x, y + 1) or
                 dfs(index + 1, x, y - 1))
        
        # Restore the original value of the cell
        board[x][y] = temp
        
        return found
    
    # Iterate through each cell in the grid
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0] and dfs(0, i, j):
                # Found the first letter and the rest of the word
                return True
                
    # Word not found in the grid
    return False

