from collections import defaultdict, deque

def topological_sort(k, conditions):
    """
    Helper function to perform topological sort based on the given conditions.
    
    Args:
    k (int): Number of nodes.
    conditions (List[List[int]]): List of edges representing conditions.
    
    Returns:
    List[int]: A list representing the topological order of nodes or an empty list if a cycle is detected.
    """
    graph = defaultdict(list)
    in_degree = [0] * (k + 1)
    
    for u, v in conditions:
        graph[u].append(v)
        in_degree[v] += 1
    
    queue = deque([i for i in range(1, k + 1) if in_degree[i] == 0])
    topo_order = []
    
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(topo_order) == k:
        return topo_order
    else:
        return []

def buildMatrix(k, rowConditions, colConditions):
    """
    Builds a k x k matrix satisfying the given row and column conditions.
    
    Args:
    k (int): Number of distinct numbers.
    rowConditions (List[List[int]]): List of row conditions.
    colConditions (List[List[int]]): List of column conditions.
    
    Returns:
    List[List[int]]: A k x k matrix satisfying the conditions or an empty list if no valid matrix exists.
    """
    row_order = topological_sort(k, rowConditions)
    col_order = topological_sort(k, colConditions)
    
    if not row_order or not col_order:
        return []
    
    row_pos = {num: i for i, num in enumerate(row_order)}
    col_pos = {num: i for i, num in enumerate(col_order)}
    
    matrix = [[0] * k for _ in range(k)]
    
    for num in range(1, k + 1):
        r = row_pos[num]
        c = col_pos[num]
        matrix[r][c] = num
    
    return matrix