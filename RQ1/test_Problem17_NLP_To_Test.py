from bisect import bisect_left, insort_left

def countSmaller(nums):
    """
    Returns an array of counts where each count is the number of smaller elements to the right of each element in the input array.
    
    :param nums: List of integers
    :return: List of counts
    """
    # This will hold the sorted list of numbers we've processed so far
    sorted_list = []
    # This will hold the results in reverse order
    result = []
    # Traverse the list from the rightmost element to the leftmost element
    for num in reversed(nums):
        # Find the index where the current number would fit in the sorted_list
        index = bisect_left(sorted_list, num)
        # Append the index to the result as it represents the number of smaller elements before the current number
        result.append(index)
        # Insert the current number into the sorted_list while maintaining order
        insort_left(sorted_list, num)
    # Since we've built the result in reverse order, we need to reverse it before returning
    return result[::-1]