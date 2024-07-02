# test file
import pytest
from Problem30_GeneratedSolution import exist  # Adjust this import based on your file structure

# Test case where the word is found along a straight line horizontally
def test_word_found_horizontal():
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    assert exist(board, word) == True, "Failed to find the word horizontally"

# Test case where the word is found along a straight line vertically
def test_word_found_vertical():
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "SEE"
    assert exist(board, word) == True, "Failed to find the word vertically"

# Test case where the word is found with a complex path
def test_word_found_complex_path():
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'E', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCESEEEFS"
    assert exist(board, word) == True, "Failed to find the word with a complex path"

# Test case where the word does not exist
def test_word_not_found():
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCB"
    assert exist(board, word) == False, "Incorrectly found a non-existent word"

# Test case for an empty grid
def test_empty_grid():
    board = []
    word = "ABCB"
    assert exist(board, word) == False, "Incorrectly found a word in an empty grid"


# Test case for a single letter word that exists
def test_single_letter_word_exists():
    board = [
        ['A']
    ]
    word = "A"
    assert exist(board, word) == True, "Failed to find a single letter word"

# Test case for a single letter word that does not exist
def test_single_letter_word_not_exists():
    board = [
        ['A']
    ]
    word = "B"
    assert exist(board, word) == False, "Incorrectly found a non-existent single letter word"

# Test case where the word is longer than any possible path in the grid
def test_word_too_long():
    board = [
        ['A', 'B'],
        ['C', 'D']
    ]
    word = "ABCDABCD"
    assert exist(board, word) == False, "Incorrectly found a word that is too long for the grid"

