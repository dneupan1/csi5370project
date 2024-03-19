
def isPathCrossing(distance):
    """
    Determine if a path crosses itself.
    
    Args:
    distance: List of integers representing the distance moved in each direction starting from (0, 0) and moving
              north, then west, south, east, and so on in a counter-clockwise direction.
    
    Returns:
    A boolean indicating whether the path crosses itself.
    """
    # Initialize the starting point.
    x, y = 0, 0
    # Add the starting point to the visited set.
    visited = set([(x, y)])
    
    # Directions are represented as (dx, dy).
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    dir_index = 0  # Start by moving north.
    
    for d in distance:
        dx, dy = directions[dir_index]
        # Update the position based on the distance moved in the current direction.
        for _ in range(d):
            x += dx
            y += dy
            # Check if the new position has been visited before.
            if (x, y) in visited:
                return True
            visited.add((x, y))
        # Change direction counter-clockwise.
        dir_index = (dir_index + 1) % 4
    
    # If the loop completes without finding any crossing, return False.
    return False
