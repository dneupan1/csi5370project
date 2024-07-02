def addOperators(num, target):
    def backtrack(index, path, value, last):
        """
        - index: Current index in num being processed.
        - path: The expression built so far.
        - value: Current value of the expression.
        - last: The last value added or subtracted in the expression.
        """
        # If we've reached the end of num and the current value equals the target, add the path to the results
        if index == len(num) and value == target:
            results.append(path)
            return
        
        for i in range(index, len(num)):
            # Avoid numbers with leading zeros
            if i > index and num[index] == '0':
                break
            
            curr = num[index:i+1]
            curr_val = int(curr)
            
            # If at the start, simply recurse without adding an operator
            if index == 0:
                backtrack(i + 1, curr, curr_val, curr_val)
            else:
                # Addition
                backtrack(i + 1, path + '+' + curr, value + curr_val, curr_val)
                # Subtraction
                backtrack(i + 1, path + '-' + curr, value - curr_val, -curr_val)
                # Multiplication
                backtrack(i + 1, path + '*' + curr, value - last + (last * curr_val), last * curr_val)
    
    results = []
    backtrack(0, "", 0, 0)
    return results

