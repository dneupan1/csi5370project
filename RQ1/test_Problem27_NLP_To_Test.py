def search(nums, target):
    """
    Search for a target value in a rotated sorted array and return its index or -1 if it's not found.
    
    Args:
    nums (List[int]): Rotated sorted array of integers with distinct values.
    target (int): The target value to search for.
    
    Returns:
    int: The index of the target in nums, or -1 if it is not found.
    
    Explanation:
    The function uses a binary search modified to account for the array's rotation. The idea is to
    identify the ordered part of the array in each iteration and check if the target can possibly be in that part.
    If it can, narrow the search to that part; otherwise, search in the other part.
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Determine if the left side is sorted
        if nums[left] <= nums[mid]:
            # Target is within the sorted left side
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right side must be sorted since left is not
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1