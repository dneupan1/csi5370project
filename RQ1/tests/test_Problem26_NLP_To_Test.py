def diffWaysToCompute(expression):
    """
    Computes all possible results from different ways of grouping numbers and operators in an expression.
    
    Args:
    expression (str): A string of numbers and operators.
    
    Returns:
    List[int]: All possible results of computations.
    
    Explanation:
    The function uses recursion to break down the expression at each operator, computing results for each part
    and combining them according to the operator. Memoization is used to store results for subexpressions to avoid redundant calculations.
    """
    memo = {}
    
    def compute(expression):
        if expression in memo:
            return memo[expression]
        if expression.isdigit():  # Base case: the expression is a pure number
            return [int(expression)]
        
        results = []
        # Recurse on every operator found in the expression
        for i, char in enumerate(expression):
            if char in '+-*':
                # Divide expression around the operator
                left = compute(expression[:i])
                right = compute(expression[i+1:])
                
                # Calculate results for all combinations of results from left and right parts
                for l in left:
                    for r in right:
                        if char == '+':
                            results.append(l + r)
                        elif char == '-':
                            results.append(l - r)
                        elif char == '*':
                            results.append(l * r)
        
        memo[expression] = results
        return results
    
    return compute(expression)