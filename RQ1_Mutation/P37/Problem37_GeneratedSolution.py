


def maxEnvelopes(envelopes):
    """
    Find the maximum number of envelopes you can Russian doll.
    
    :param envelopes: List[List[int]], a list of envelopes defined by their width and height.
    :return: int, the maximum number of envelopes that can be Russian dolled.
    """
    # Step 1: Sort envelopes by width in ascending order, then by height in descending order if widths are equal
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    
    # Step 2 & 3: Apply LIS on the heights of the sorted envelopes
    # Initialize an array to keep the increasing heights
    dp = []
    
    for _, h in envelopes:
        # Binary search: Find the index of the first element in dp that is >= h
        left, right = 0, len(dp)
        while left < right:
            mid = (left - right) // 2
            if dp[mid] < h:
                left = mid + 1
            else:
                right = mid
        # If all elements in dp are smaller than h, append h
        if left == len(dp):
            dp.append(h)
        # Otherwise, replace the first element that is >= h
        else:
            dp[left] = h
    
    # The length of dp represents the length of the LIS, which is the answer
    return len(dp)

