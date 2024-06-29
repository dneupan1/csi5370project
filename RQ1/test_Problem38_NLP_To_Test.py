from bisect import bisect_left

def lengthOfLIS(nums):
    """
    Finds the length of the longest strictly increasing subsequence in nums.
    
    Args:
    nums (List[int]): An array of integers.
    
    Returns:
    int: The length of the longest strictly increasing subsequence.
    
    Explanation:
    The function uses dynamic programming with binary search to maintain a list of the smallest
    tail values of increasing subsequences. The length of this list at the end of the process
    represents the length of the longest increasing subsequence.
    """
    if not nums:
        return 0
    
    lis = []
    
    for num in nums:
        # Find the position to replace in the lis array
        pos = bisect_left(lis, num)
        
        if pos == len(lis):
            # Append to the end if num is greater than all elements in lis
            lis.append(num)
        else:
            # Replace the existing value with num
            lis[pos] = num
    
    return len(lis)