


from collections import defaultdict, deque

def topological_sort(k, conditions):
    graph = defaultdict(list)
    in_degree = {i: 0 for i in range(1, k + 1)}
    
    # Build graph
    for u, v in conditions:
        graph[u].append(v)
        in_degree[v] += 1

    # Perform topological sort
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    sorted_order = []
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if topological sort is possible (i.e., no cycle)
    if len(sorted_order) == k:
        return sorted_order
    else:
        return []

def buildMatrix(k, rowConditions, colConditions):
    # Get topological sort for rows and columns
    row_order = topological_sort(k, rowConditions)
    col_order = topological_sort(k, colConditions)
    
    if not row_order or not col_order:  # Impossible to satisfy the conditions
        return []
    
    # Create a mapping from number to its position in the order
    row_pos = {num: i for i, num in enumerate(row_order)}
    col_pos = {num: i for i, num in enumerate(col_order)}
    
    # Initialize matrix with zeros
    matrix = [[0 for _ in range(k)] for _ in range(k)]
    
    # Place the numbers in the matrix according to the sorted orders
    for num in range(1, k + 1):
        matrix[row_pos[num]][col_pos[num]] = num
        
    return matrix

