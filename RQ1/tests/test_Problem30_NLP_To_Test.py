import pytest
from Problem30_GeneratedSolution import exist  # Assuming the function 'exist' is defined in 'solution.py'

@pytest.mark.parametrize("board, word, expected", [
    # Example 1: Word can be formed following a complex path
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
    # Example 2: Word can be formed following a simple vertical path
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
    # Example 3: Word cannot be formed because it would require reusing a cell
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False),
    # Word is longer than the number of cells in the grid
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCDEFGHIJKLMN", False),
    # Grid with one cell, positive case
    ([["A"]], "A", True),
    # Grid with one cell, negative case
    ([["A"]], "B", False),
    # Grid where word is in a horizontal line
    ([["A","B","C","D","E"]], "ABCDE", True),
    # Grid where word is in a vertical line
    ([["A"],["B"],["C"],["D"],["E"]], "ABCDE", True),
    # Grid where word wraps around the edge (should be false)
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ECBA", False),
    # Empty grid
    ([], "ABC", False),
    # Large grid with no valid path
    ([["A","B","C","D","E"]*5]*5, "FEDCBA", False)
])
def test_exist(board, word, expected):
    """
    Tests the exist function with various boards and words to ensure it correctly identifies whether the word can be formed from the board.

    This test function verifies:
    - The ability to handle a range of board configurations, from simple to complex and varying sizes.
    - The capability to correctly follow the rules of adjacency and non-reuse of cells.
    - Correct behavior for edge cases such as an empty board, or a board with only one cell.

    Args:
    board (list of list of str): The m x n grid of characters representing the board.
    word (str): The word to be searched for in the board.
    expected (bool): Expected result indicating whether the word can be formed or not.
    """
    assert exist(board, word) == expected, f"Test failed for board={board}, word={word}. Expected {expected}, got {exist(board, word)}"
