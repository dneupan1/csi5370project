def maximalPathQuality(values, edges, maxTime):
    # Step 1: Build the graph as an adjacency list
    graph = {}
    for u, v, time in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, time))
        graph[v].append((u, time))
    
    # Step 2: Initialize the maximum quality found
    maxQuality = 0
    
    # Step 3: DFS function to explore all paths
    def dfs(node, time, visited, quality):
        nonlocal maxQuality
        # Update the quality and maxQuality if returning to node 0
        if node == 0:
            maxQuality = max(maxQuality, quality)
        # Explore all neighbors
        for neighbor, travelTime in graph.get(node, []):
            nextTime = time + travelTime
            if nextTime <= maxTime:
                # If the neighbor hasn't been visited, add its value to the quality
                if neighbor not in visited:
                    dfs(neighbor, nextTime, visited | {neighbor}, quality + values[neighbor])
                else:
                    dfs(neighbor, nextTime, visited, quality)
    
    # Step 4: Start DFS from node 0 with initial values
    dfs(0, 0, {0}, values[0])
    
    return maxQuality

