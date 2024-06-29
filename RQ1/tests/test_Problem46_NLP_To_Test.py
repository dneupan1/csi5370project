from typing import List

def increasingTriplet(nums: List[int]) -> bool:
    """
    This function returns true if there exists a triple of indices (i, j, k)
    such that i < j < k and nums[i] < nums[j] < nums[k]. Otherwise, it returns false.
    
    :param nums: List[int] - List of integers
    :return: bool - True if such a triplet exists, False otherwise
    """
    
    # Initialize two variables to represent the smallest and second smallest values found so far
    first = float('inf')
    second = float('inf')
    
    # Traverse through the list
    for num in nums:
        if num <= first:
            first = num  # Update the smallest value
        elif num <= second:
            second = num  # Update the second smallest value
        else:
            # If we find a number greater than both first and second, we found a triplet
            return True
    
    # If we complete the loop without finding such a triplet, return False
    return False