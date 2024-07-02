
def isRectangleCover(rectangles):
    """
    Check if the given rectangles form an exact cover of a rectangular region.

    Args:
    rectangles: List of lists, where each inner list contains 4 integers representing a rectangle.

    Returns:
    A boolean indicating whether the rectangles form an exact cover.
    """
    # Initialize variables to track the bounding rectangle's corners and the total area.
    minX, minY, maxX, maxY = float('inf'), float('inf'), float('-inf'), float('-inf')
    area = 0
    corners = set()

    for rect in rectangles:
        x1, y1, x2, y2 = rect
        # Update bounding rectangle corners.
        minX, minY, maxX, maxY = min(minX, x1), min(minY, y1), max(maxX, x2), max(maxY, y2)
        # Update total area.
        area += (x2 - x1) * (y2 - y1)
        # Update corners set.
        for point in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
            if point in corners:
                corners.remove(point)
            else:
                corners.add(point)

    # Check if the total area of the rectangles equals the area of the bounding rectangle.
    if area != (maxX - minX) * (maxY - minY):
        return False

    # Check if the corners set only contains the corners of the bounding rectangle.
    if len(corners) != 4 or not all(point in corners for point in [(minX, minY), (minX, maxY), (maxX, minY), (maxX, maxY)]):
        return False

    return True
