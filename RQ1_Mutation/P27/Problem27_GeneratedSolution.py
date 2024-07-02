

def search(nums, target):
    """
    This function performs a modified binary search on a rotated sorted array
    to find the index of a given target. If the target is not found, it returns -1.
    
    The function uses binary search but adjusts the conditions to accommodate
    the rotation of the array. It determines which part of the array (left or right
    half) is normally ordered and then checks if the target lies within that range,
    adjusting the search bounds accordingly.
    
    :param nums: List[int], a rotated sorted array.
    :param target: int, the target value to search for.
    :return: int, the index of target if found, otherwise -1.
    """
    
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # If the target is found
        if nums[mid] == target:
            return mid
        
        # If the left half is normally ordered
        if nums[left] <= nums[mid]:
            # Check if the target is within the normally ordered left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Narrow down to the left half
            else:
                left = mid + 1   # Otherwise, target must be in the right half
        else:
            # If the right half is normally ordered
            # Check if the target is within the normally ordered right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # Narrow down to the right half
            else:
                right = mid - 1  # Otherwise, target must be in the left half
                
    # If the target is not found
    return -1

