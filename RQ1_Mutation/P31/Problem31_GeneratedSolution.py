def findOrder(numCourses, prerequisites):
    """
    Find an order of courses to finish all courses given the prerequisites.
    
    :param numCourses: int, the total number of courses.
    :param prerequisites: List[List[int]], the prerequisite pairs where each pair [a, b]
                          indicates that course b is a prerequisite for course a.
    :return: List[int], an ordering of courses that allows you to finish all courses,
             or an empty list if it is impossible.
    """
    # Create adjacency list for each course
    adj_list = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        adj_list[course].append(prereq)
    
    # Visited set to keep track of visited courses during DFS
    visited = set()
    # Track courses being explored to detect cycles
    exploring = set()
    # Stack to maintain the correct order of courses
    order = []
    
    def dfs(course):
        """Depth-first search to explore prerequisites."""
        if course in exploring:
            # Cycle detected
            return False
        if course in visited:
            # Already visited and no cycles detected along this path
            return True
        
        # Mark the current node as exploring
        exploring.add(course)
        for prereq in adj_list[course]:
            if not dfs(prereq):
                return False
        # Mark the current node as visited
        exploring.remove(course)
        visited.add(course)
        # Add to stack to maintain ordering
        order.append(course)
        return True
    
    # Run DFS from each course
    for course in range(numCourses):
        if not dfs(course):
            # If a cycle is detected, return an empty list
            return []
    
    # If all courses are visited without detecting a cycle, return the order
    return order
