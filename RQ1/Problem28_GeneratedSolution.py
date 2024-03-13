
def firstMissingPositive(nums):
    """
    Finds the smallest missing positive integer in an unsorted array.
    
    This function re-arranges the numbers in the array such that each number
    is placed at its corresponding index (e.g., 1 at index 0, 2 at index 1, etc.).
    Then, it iterates through the list to find the first index not following
    this rule, which represents the smallest missing positive integer.
    
    :param nums: List[int], an unsorted array of integers.
    :return: int, the smallest missing positive integer.
    """
    n = len(nums)
    
    for i in range(n):
        # Swap until each number is in its correct place or until an unswappable condition is met
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # Swap nums[i] with the number at its "correct" position
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    
    # Find the first number missing from its place
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    # If all positions are correctly filled, the missing number is n+1
    return n + 1
