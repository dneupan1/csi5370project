from typing import List

def canCross(stones: List[int]) -> bool:
    """
    This function determines if the frog can cross the river by landing on the last stone.
    :param stones: List[int] - A list of stone positions in sorted ascending order
    :return: bool - True if the frog can cross the river, False otherwise
    """
    
    # Early exit if the first jump is more than 1 unit (invalid starting condition)
    if stones[1] != 1:
        return False
    
    # Dictionary to hold the positions and the set of jump distances that can reach that position
    stone_positions = {stone: set() for stone in stones}
    # The frog starts on the first stone with a jump of 0 units
    stone_positions[0].add(0)
    
    # Iterate through each stone
    for stone in stones:
        for last_jump in stone_positions[stone]:
            # Try jumps of last_jump-1, last_jump, last_jump+1 units
            for jump in [last_jump - 1, last_jump, last_jump + 1]:
                if jump > 0 and (stone + jump) in stone_positions:
                    stone_positions[stone + jump].add(jump)
    
    # Check if there are any jumps that can reach the last stone
    return bool(stone_positions[stones[-1]])