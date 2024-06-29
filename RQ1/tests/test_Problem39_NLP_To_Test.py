from collections import deque

def is_valid(s):
    """
    Helper function to check if a string has valid parentheses.
    """
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0

def removeInvalidParentheses(s):
    """
    Removes the minimum number of invalid parentheses to make the input string valid.
    
    Args:
    s (str): The input string containing parentheses and letters.
    
    Returns:
    List[str]: A list of unique valid strings with the minimum number of removals.
    """
    if not s:
        return [""]
    
    # Initialize BFS
    queue = deque([s])
    visited = set([s])
    found = False
    valid_expressions = []
    
    while queue:
        current_level_size = len(queue)
        current_level_expressions = []
        
        for _ in range(current_level_size):
            current = queue.popleft()
            
            if is_valid(current):
                found = True
                current_level_expressions.append(current)
            
            if found:
                continue
            
            # Generate all possible states
            for i in range(len(current)):
                if current[i] not in ('(', ')'):
                    continue
                next_state = current[:i] + current[i+1:]
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append(next_state)
        
        if found:
            valid_expressions.extend(current_level_expressions)
    
    return valid_expressions