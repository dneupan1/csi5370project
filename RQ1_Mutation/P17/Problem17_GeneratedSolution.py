def countSmaller(nums):
    def merge_sort(indices):
        half = len(indices) // 2
        if half:
            left, right = merge_sort(indices[:half]), merge_sort(indices[half:])
            for i in range(len(indices))[::-1]:
                if not right or left and nums[left[-1]] > nums[right[-1]]:
                    counts[left[-1]] += len(right)
                    indices[i] = left.pop()
                else:
                    indices[i] = right.pop()
        return indices
    
    counts = [0] * len(nums)
    merge_sort(list(range(len(nums))))
    return counts

