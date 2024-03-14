
def maxCoins(nums):
    """
    Calculate the maximum coins that can be collected by bursting balloons wisely.
    
    :param nums: List[int], numbers painted on balloons.
    :return: int, maximum coins collected.
    """
    # Extend nums by adding 1 on both ends to simplify calculations
    nums = [1] + nums + [1]
    n = len(nums)
    # Initialize dp array
    dp = [[0] * n for _ in range(n)]
    
    # Fill dp array
    for length in range(2, n):  # Start with subarrays of length 2
        for left in range(0, n - length):
            right = left + length
            # Choose the last balloon to burst in the subarray nums[left:right+1]
            for i in range(left + 1, right):
                # Calculate max coins if the ith balloon is the last to burst
                coins = nums[left] * nums[i] * nums[right]
                total = coins + dp[left][i] + dp[i][right]
                dp[left][right] = max(dp[left][right], total)
    
    # Result is the max coins for bursting all balloons
    return dp[0][n-1]

