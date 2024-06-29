def fourSum(nums: list[int], target: int) -> list[list[int]]:
    """
    This function finds all unique quadruplets in the array that sum up to the target value.

    :param nums: List of integers
    :param target: Target sum for the quadruplets
    :return: List of unique quadruplets that sum up to the target
    """
    # Sort the array to simplify the two-pointer approach
    nums.sort()
    # Result list to store the unique quadruplets
    result = []
    # Length of the input array
    n = len(nums)

    # Iterate through the array with the first pointer
    for i in range(n - 3):
        # Skip duplicate elements for the first pointer
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # Iterate through the array with the second pointer
        for j in range(i + 1, n - 2):
            # Skip duplicate elements for the second pointer
            if j > 0 and nums[j] == nums[j - 1] and j > i + 1:
                continue
            # Initialize the two pointers for the two-pointer approach
            left, right = j + 1, n - 1
            # Use the two-pointer approach to find pairs that sum up to the remaining target
            while left < right:
                # Calculate the current sum of the four elements
                total = nums[i] + nums[j] + nums[left] + nums[right]
                # If the sum matches the target, add the quadruplet to the result
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    # Move the left pointer to the right and skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Move the right pointer to the left and skip duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # Move both pointers
                    left += 1
                    right -= 1
                # If the sum is less than the target, move the left pointer to the right
                elif total < target:
                    left += 1
                # If the sum is greater than the target, move the right pointer to the left
                else:
                    right -= 1

    # Return the result list with all unique quadruplets
    return result