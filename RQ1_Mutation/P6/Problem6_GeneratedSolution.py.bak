def fourSum(nums, target):
    # Step 1: Sort the array
    nums.sort()
    result = []
    
    # Step 2: Iterate over the array with two loops
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # Skip duplicate numbers
        for j in range(i+1, len(nums) - 2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue  # Skip duplicate numbers
                
            # Step 3: Two-pointer technique
            left, right = j + 1, len(nums) - 1
            while left < right:
                quad_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if quad_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    # Step 4: Avoid duplicates for the third and fourth numbers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif quad_sum < target:
                    left += 1
                else:
                    right -= 1
                    
    # Step 5: Return the result
    return result
