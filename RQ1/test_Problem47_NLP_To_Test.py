from typing import List

def isSelfCrossing(distance: List[int]) -> bool:
    """
    This function returns true if the path crosses itself, otherwise false.
    
    :param distance: List[int] - List of distances representing the moves in the order:
                      north, west, south, east, and so on.
    :return: bool - True if the path crosses itself, False otherwise
    """
    
    # Check if the distance list has less than 4 moves, which cannot form a crossing
    if len(distance) < 4:
        return False
    
    # Iterate through the distance array starting from the 4th element
    for i in range(3, len(distance)):
        # Case 1: Fourth line crosses first line
        if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
            return True
        # Case 2: Fifth line crosses first line
        if i >= 4 and distance[i - 1] == distance[i - 3] and distance[i] + distance[i - 4] >= distance[i - 2]:
            return True
        # Case 3: Sixth line crosses first line
        if i >= 5 and distance[i - 2] >= distance[i - 4] and distance[i] + distance[i - 4] >= distance[i - 2] and distance[i - 1] <= distance[i - 3] and distance[i - 1] + distance[i - 5] >= distance[i - 3]:
            return True
    
    # If no crossing is detected, return False
    return False