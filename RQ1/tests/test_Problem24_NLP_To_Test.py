def findTargetSumWays(nums, target):
    """
    Computes the number of ways to assign '+' and '-' symbols to make the sum of nums equal to target.
    
    Args:
    nums (List[int]): List of integers.
    target (int): The target sum to achieve.
    
    Returns:
    int: Number of ways to achieve the target sum.
    
    Explanation:
    We use a dictionary to keep track of all possible sums we can achieve at each step along with their counts.
    We update this dictionary as we process each number in nums by considering both adding and subtracting it.
    """
    # Initialize a dictionary to store the count of ways to achieve each sum
    dp = {0: 1}  # There is one way to achieve a sum of 0 - by using no elements

    # Iterate over each number in the array
    for num in nums:
        next_dp = {}
        # Update the dp dictionary for each possible sum we have so far
        for sum_val, count in dp.items():
            next_dp[sum_val + num] = next_dp.get(sum_val + num, 0) + count
            next_dp[sum_val - num] = next_dp.get(sum_val - num, 0) + count
        dp = next_dp  # Move to the next state

    # Return the count of ways we can achieve the target sum
    return dp.get(target, 0)