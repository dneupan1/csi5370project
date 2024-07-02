def canPartition(nums):
    totalSum = sum(nums)
    
    # If totalSum is odd, it's not possible to partition it into two equal subsets
    if totalSum % 2 != 0:
        return False
    
    # The target sum each subset should reach
    target = totalSum // 2
    
    # Initialize DP table. dp[i] will be True if subset sum i is achievable
    dp = [False] * (target + 1)
    dp[0] = True  # Base case: sum of 0 is always achievable
    
    # Update DP table based on nums
    for num in nums:
        # Iterate backwards to avoid using the same element more than once
        for i in range(target, num - 1, -1):
            if dp[i - num]:
                dp[i] = True
                
    return dp[target]

