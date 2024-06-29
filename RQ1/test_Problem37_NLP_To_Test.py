from bisect import bisect_left

def maxEnvelopes(envelopes):
    """
    Finds the maximum number of envelopes that can be Russian dolled (nested inside each other).
    
    Args:
    envelopes (List[List[int]]): A list of envelopes represented by their width and height.
    
    Returns:
    int: The maximum number of envelopes that can be nested.
    
    Explanation:
    The function sorts the envelopes and then applies a LIS (Longest Increasing Subsequence) algorithm
    on the heights of the sorted envelopes.
    """
    if not envelopes:
        return 0
    
    # Sort envelopes: first by width (asc), then by height (desc) if widths are the same
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    
    # Extract the heights of the sorted envelopes
    heights = [h for _, h in envelopes]
    
    # Find the LIS in the heights array
    lis = []
    for h in heights:
        pos = bisect_left(lis, h)
        if pos == len(lis):
            lis.append(h)
        else:
            lis[pos] = h
    
    return len(lis)