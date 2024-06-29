import heapq

def trapRainWater(heightMap):
    """
    This function calculates the total volume of water trapped after raining on a 2D elevation map.
    
    Args:
    heightMap (List[List[int]]): A matrix of integers representing the height of each cell.
    
    Returns:
    int: The total volume of trapped water.
    
    Explanation:
    The problem is solved using a min-heap (priority queue) to always expand the smallest height on the perimeter
    and a visited set to keep track of cells that have already been processed. The key is to work inward from the
    perimeter, calculating potential trapped water at each step.
    """
    
    if not heightMap or not heightMap[0]:
        return 0

    m, n = len(heightMap), len(heightMap[0])
    visited = set()
    heap = []

    # Initialize the heap with the perimeter cells of the matrix
    for i in range(m):
        for j in [0, n-1]:
            heapq.heappush(heap, (heightMap[i][j], i, j))
            visited.add((i, j))
    for j in range(n):
        for i in [0, m-1]:
            if (i, j) not in visited:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited.add((i, j))

    result = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while heap:
        height, x, y = heapq.heappop(heap)

        # Explore the four neighboring cells
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                # Calculate trapped water for the current cell
                result += max(0, height - heightMap[nx][ny])
                # Push the max height of the current or the neighboring cell onto the heap
                heapq.heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))

    return result