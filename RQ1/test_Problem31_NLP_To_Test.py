from collections import defaultdict, deque

def findOrder(numCourses, prerequisites):
    """
    Finds an order in which to take the courses given their prerequisites.
    
    Args:
    numCourses (int): Total number of courses.
    prerequisites (List[List[int]]): Prerequisite pairs.
    
    Returns:
    List[int]: A list representing the order of courses to take, or an empty list if impossible.
    
    Explanation:
    The function uses Kahn's algorithm for topological sorting with BFS to determine a valid course order.
    """
    # Build the adjacency list for the graph and count in-degrees of each node
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    
    for dest, src in prerequisites:
        graph[src].append(dest)
        in_degree[dest] += 1
    
    # Queue for nodes with no incoming edges (in-degree of 0)
    zero_in_degree_queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    
    topological_order = []
    
    while zero_in_degree_queue:
        node = zero_in_degree_queue.popleft()
        topological_order.append(node)
        
        # Decrease in-degree of neighbors
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            # If in-degree becomes 0, add to the queue
            if in_degree[neighbor] == 0:
                zero_in_degree_queue.append(neighbor)
    
    # If we have added all courses to the topological order, return it
    if len(topological_order) == numCourses:
        return topological_order
    else:
        # There is a cycle, so it's impossible to complete all courses
        return []