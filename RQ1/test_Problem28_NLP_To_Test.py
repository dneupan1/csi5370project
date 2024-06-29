def firstMissingPositive(nums):
    """
    Finds the smallest positive integer that is not present in the array.
    
    Args:
    nums (List[int]): An unsorted list of integers.
    
    Returns:
    int: The smallest positive integer that is missing from the array.
    
    Explanation:
    The solution involves normalizing the array, marking the presence of integers using indices,
    and then determining the smallest missing positive by checking these marks.
    """
    n = len(nums)
    # Normalize the array (step 1)
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
    
    # Mark the indices (step 2)
    for i in range(n):
        val = abs(nums[i])
        if val <= n:
            nums[val - 1] = -abs(nums[val - 1])
    
    # Determine the smallest missing positive (step 3)
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    
    # If all positions are filled, the missing number is n+1
    return n + 1
