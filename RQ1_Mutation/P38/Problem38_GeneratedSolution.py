


def lengthOfLIS(nums):
    """
    Find the length of the longest strictly increasing subsequence.
    
    :param nums: List[int], a list of integers.
    :return: int, the length of the longest increasing subsequence.
    """
    if not nums:
        return 0
    
    # Initialize DP array
    dp = [1] * len(nums)
    
    # Fill DP array
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Find the maximum in DP array
    return max(dp)

