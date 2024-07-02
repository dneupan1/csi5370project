def findTargetSumWays(nums, target):
    """
    Calculate the number of ways to assign '+' and '-' symbols to make the sum of nums equal to target.
    
    Args:
    nums: List of integers.
    target: Integer target sum.
    
    Returns:
    The number of different expressions that evaluate to target.
    """
    totalSum = sum(nums)
    
    # If target is absolutely larger than the totalSum or (target + totalSum) is odd, there's no solution
    if abs(target) > totalSum or (target + totalSum) % 2 == 1:
        return 0
    
    # Transform the problem into a subset sum problem
    subsetSum = (target + totalSum) // 2
    
    # Initialize dp array: dp[i] will store the count of subsets that sum up to i
    dp = [0] * (subsetSum + 1)
    dp[0] = 1  # There's 1 way to achieve sum 0: by choosing no element
    
    # Fill dp array
    for num in nums:
        # Traverse in reverse to ensure each number is only used once
        for i in range(subsetSum, num - 1, -1):
            dp[i] += dp[i - num]
    
    return dp[subsetSum]
