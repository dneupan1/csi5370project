def diffWaysToCompute(expression):
    """
    Compute all possible results from computing all the different possible ways
    to group numbers and operators in the given expression.
    """
    # Memoization cache
    memo = {}
    
    def compute(expression):
        # Check if the result for this expression is already computed
        if expression in memo:
            return memo[expression]
        
        # Try to convert the expression directly to an integer (base case)
        if expression.isdigit():
            return [int(expression)]
        
        results = []
        # Iterate through the expression to find operators and split the expression
        for i, char in enumerate(expression):
            if char in "+-*":
                # Compute left and right sub-expressions
                left = compute(expression[:i])
                right = compute(expression[i+1:])
                
                # Combine the results from left and right sub-expressions
                for l in left:
                    for r in right:
                        if char == '+':
                            results.append(l + r)
                        elif char == '-':
                            results.append(l - r)
                        elif char == '*':
                            results.append(l * r)
        
        # Store the computed result in memo before returning
        memo[expression] = results
        return results
    
    # Start the recursion
    return compute(expression)