
def rob_linear(nums):
    """
    Solves the House Robber problem for a linear array of houses.
    
    :param nums: List[int], the amount of money at each house.
    :return: int, the maximum amount of money that can be robbed.
    """
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])
    
    return dp[-1]

def rob(nums):
    """
    Solves the House Robber II problem for a circular array of houses.
    
    The solution involves solving two House Robber problems:
    1. Excluding the first house.
    2. Excluding the last house.
    
    :param nums: List[int], the amount of money at each house.
    :return: int, the maximum amount of money that can be robbed without alerting the police.
    """
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums)
    
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

