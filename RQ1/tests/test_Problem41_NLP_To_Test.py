def maxCoins(nums):
    """
    Returns the maximum coins that can be collected by bursting the balloons wisely.
    
    Args:
    nums (List[int]): A list of integers representing the balloons with numbers painted on them.
    
    Returns:
    int: The maximum coins that can be collected.
    """
    n = len(nums)
    nums = [1] + nums + [1]  # Add 1 at both ends to simplify boundary conditions
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    
    # Fill DP table
    for length in range(1, n + 1):  # Length of the subarray
        for left in range(1, n - length + 2):  # Starting index of the subarray
            right = left + length - 1  # Ending index of the subarray
            for k in range(left, right + 1):  # Position of the last balloon to burst in subarray
                dp[left][right] = max(
                    dp[left][right],
                    nums[left - 1] * nums[k] * nums[right + 1] + dp[left][k - 1] + dp[k + 1][right]
                )
    
    return dp[1][n]