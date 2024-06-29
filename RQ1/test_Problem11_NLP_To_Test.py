from collections import defaultdict, deque

def maxPathQuality(values, edges, maxTime):
    """
    This function returns the maximum quality of a valid path in an undirected graph
    given the node values, edges, and maximum allowed time.

    :param values: List of integers representing the value of each node
    :param edges: List of lists representing the edges between nodes and travel times
    :param maxTime: Integer representing the maximum allowed travel time
    :return: Maximum quality of a valid path
    """
    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for u, v, time in edges:
        graph[u].append((v, time))
        graph[v].append((u, time))

    n = len(values)
    max_quality = 0
    visited = [0] * n

    def dfs(node, current_time, current_quality):
        nonlocal max_quality

        if current_time > maxTime:
            return
        
        if visited[node] == 0:
            current_quality += values[node]

        if node == 0:
            max_quality = max(max_quality, current_quality)

        visited[node] += 1

        for neighbor, travel_time in graph[node]:
            dfs(neighbor, current_time + travel_time, current_quality)

        visited[node] -= 1

    dfs(0, 0, 0)

    return max_quality