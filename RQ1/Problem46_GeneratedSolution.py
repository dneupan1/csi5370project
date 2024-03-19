
def increasingTriplet(nums):
    """
    Check if there exists an increasing triplet in the list.
    
    This function uses a two-pointer approach to keep track of the smallest and second smallest values seen so far.
    It iterates through the list once, updating these values as needed. If it finds a value greater than both,
    it means an increasing triplet exists.
    
    Args:
    nums: List of integers.
    
    Returns:
    A boolean indicating whether an increasing triplet exists.
    """
    # Initialize two variables to track the smallest and second smallest numbers.
    # Use float('inf') for initialization to handle all possible integer values in the input.
    first = second = float('inf')
    
    for n in nums:
        # If the current number is smaller than the smallest seen so far, update 'first'.
        if n <= first:
            first = n
        # If the current number is between 'first' and 'second', update 'second'.
        elif n <= second:
            second = n
        # If the current number is larger than both 'first' and 'second', an increasing triplet exists.
        else:
            return True
    # If no such triplet is found, return False.
    return False

