import pytest
from Problem49_GeneratedSolution import isRectangleCover as is_exact_cover  # Assuming the function to be tested is named 'is_exact_cover' and is in 'solution.py'

@pytest.mark.parametrize("rectangles, expected", [
    ([[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]], True),
    ([[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]], False),
    ([[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]], False),
    ([[0, 0, 1, 1]], True),  # Single rectangle covers the region exactly
    ([[1, 1, 2, 2], [2, 1, 3, 2], [1, 2, 3, 3]], True),  # Multiple rectangles covering without overlap or gaps
    ([[1, 1, 2, 2], [2, 1, 3, 2], [1, 2, 3, 3], [1, 1, 1.5, 1.5]], False),  # Overlapping rectangles
    ([[0, 0, 1, 1], [1, 1, 2, 2]], False)  # Rectangles not contiguous
])
def test_is_exact_cover(rectangles, expected):
    """
    Tests whether the given set of rectangles forms an exact cover of a rectangular region.

    This function utilizes parametrized testing to validate multiple scenarios:
    1. Exact coverage with no gaps or overlaps.
    2. Rectangles leaving gaps in coverage.
    3. Rectangles overlapping with each other.
    4. Edge cases with minimal rectangles or contiguity issues.

    Args:
    rectangles (list of list of int): List of rectangles defined as [xi, yi, ai, bi].
    expected (bool): Expected boolean result if rectangles form an exact cover or not.
    """
    assert is_exact_cover(rectangles) == expected, f"Failed on input {rectangles}"
