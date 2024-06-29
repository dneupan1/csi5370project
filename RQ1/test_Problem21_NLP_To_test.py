def countGreatPartitions(nums, k):
    """
    Counts the number of distinct great partitions where each partition has a sum greater than or equal to k.
    
    Args:
    nums (List[int]): List of positive integers.
    k (int): Minimum sum required for each partition to be considered great.
    
    Returns:
    int: Number of distinct great partitions modulo 10**9 + 7.
    
    Explanation:
    We use bitmasking to generate all possible partitions of the array into two groups.
    Each bit in the bitmask represents whether the element at that index belongs to the first or second group.
    We then check if both groups have a sum >= k. If they do, we increment the count.
    """
    MOD = 10**9 + 7
    n = len(nums)
    count = 0

    # Iterate over all possible partitions using bitmasking
    for mask in range(1, 1 << n):
        sum1 = sum2 = 0
        
        # Determine sums of two groups based on the bitmask
        for i in range(n):
            if mask & (1 << i):
                sum1 += nums[i]
            else:
                sum2 += nums[i]

        # Check if both partitions are "great"
        if sum1 >= k and sum2 >= k:
            count += 1

    # The result needs to be divided by 2 because each partition is counted twice
    return count // 2 % MOD