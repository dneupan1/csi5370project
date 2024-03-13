


def rotate(matrix):
    """
    Rotate the matrix by 90 degrees (clockwise) in-place.
    
    First, transpose the matrix by swapping elements across the diagonal.
    Then, reverse each row to achieve the 90-degree rotation.
    
    :param matrix: List[List[int]], a 2D matrix representing an image.
    """
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):  # Start from 'i' to swap only elements above the diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for row in matrix:
        row.reverse()  # In-place reversal of each row
    
    

