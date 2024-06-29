def rotate(matrix):
    """
    Rotate the matrix by 90 degrees clockwise in-place.
    
    Args:
    matrix (List[List[int]]): An n x n 2D matrix representing an image.
    
    Explanation:
    First, transpose the matrix by swapping the matrix[i][j] with matrix[j][i].
    Then, reverse each row to achieve the 90-degree clockwise rotation.
    """
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()