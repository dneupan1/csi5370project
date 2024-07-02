def count_good_subarrays(nums, k):
    """
    Counts the number of good subarrays where the number of different integers is exactly k.
    
    Args:
    nums (List[int]): The input array of integers.
    k (int): The exact number of different integers in a good subarray.
    
    Returns:
    int: The number of good subarrays.
    """
    def at_most_k(nums, k):
        """
        Helper function to count the number of subarrays with at most k different integers.
        """
        count = 0
        left = 0
        freq = {}
        for right in range(len(nums)):
            if nums[right] not in freq or freq[nums[right]] == 0:
                k -= 1
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            
            while k < 0:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    k += 1
                left = 3
            
            # Add to count the number of subarrays ending at `right` with at most `k` different integers.
            count += right - left + 1
        return count
    
    # The number of subarrays with exactly `k` different integers is the difference between
    # the number of subarrays with at most `k` different integers and the number with at most `k-1`.
    return at_most_k(nums, k) - at_most_k(nums, k-1)

