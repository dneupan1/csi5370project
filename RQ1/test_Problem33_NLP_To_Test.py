def rob_linear(nums):
    """
    Helper function to solve the linear house robber problem.
    
    Args:
    nums (List[int]): A list of integers representing the amount of money in each house.
    
    Returns:
    int: The maximum amount of money that can be robbed without robbing two adjacent houses.
    """
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[-1]

def rob(nums):
    """
    Solves the circular house robber problem.
    
    Args:
    nums (List[int]): A list of integers representing the amount of money in each house.
    
    Returns:
    int: The maximum amount of money that can be robbed without robbing two adjacent houses.
    """
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    
    # Compare the maximum money by robbing either from 0 to n-2 or from 1 to n-1
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))