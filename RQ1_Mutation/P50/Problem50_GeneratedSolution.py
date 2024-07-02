
def canCross(stones):
    """
    Determine if the frog can cross the river by landing on the last stone.

    Args:
    stones: List of integers representing the positions of the stones.

    Returns:
    A boolean indicating whether the frog can cross the river.
    """
    # Edge case: The second stone is too far.
    if stones[1] != 1:
        return False

    stoneSet = set(stones)  # Convert the list to a set for O(1) lookup.
    lastStone = stones[-1]  # Target position.
    memo = {}  # Memoization to store previously computed results.

    def dfs(position, jump):
        """
        Depth-first search to determine if the frog can reach the last stone from the current position.

        Args:
        position: Current position of the frog.
        jump: The last jump distance.

        Returns:
        A boolean indicating whether the frog can reach the last stone from the current position.
        """
        # Check memoization.
        if (position, jump) in memo:
            return memo[(position, jump)]

        # Base case: Frog has reached the last stone.
        if position == lastStone:
            return True

        # Try all possible next jumps: k-1, k, k+1
        for nextJump in [jump - 1, jump, jump + 1]:
            nextPosition = position + nextJump
            if nextJump > 0 and nextPosition in stoneSet and dfs(nextPosition, nextJump):
                memo[(position, jump)] = True
                return True

        # If no path found, memoize and return False.
        memo[(position, jump)] = False
        return False

    # Initial call to dfs from the first stone with an initial jump of 1.
    return dfs(1, 1)

