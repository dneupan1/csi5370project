def canPartition(nums):
    """
    Determines if the given list of numbers can be partitioned into two subsets with equal sums.
    
    Args:
    nums (List[int]): List of integers.
    
    Returns:
    bool: True if the array can be partitioned into two subsets with equal sums, False otherwise.
    
    Explanation:
    We first check if the total sum of the array is even because two equal partitions imply an even sum.
    We then use a dynamic programming approach where we keep a set of possible sums up to half of the total sum.
    If half of the total sum can be achieved with some subset of the elements, then the array can be partitioned as required.
    """
    total_sum = sum(nums)
    
    # If the total sum is odd, it's not possible to split into two equal parts
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    possible_sums = {0}  # A set to store possible sums up to the target
    
    # Iterate through each number in the array
    for num in nums:
        # We need to iterate from the target down to num to avoid reuse of the same element
        new_sums = set()
        for s in possible_sums:
            new_sum = s + num
            if new_sum == target:
                return True  # Early exit if target is reached
            if new_sum < target:
                new_sums.add(new_sum)
        possible_sums.update(new_sums)
    
    # If no subset sums to the target, the partition isn't possible
    return False