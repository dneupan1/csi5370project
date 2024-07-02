def countPrefixAligned(flips):
    # Initialize variables to keep track of the maximum integer seen and the count of prefix-aligned occurrences.
    max_seen = 0
    count_aligned = 0
    flipped_set = set()  # To track unique flips.
    
    for flip in flips:
        # Add the current flip to the set of flipped integers.
        flipped_set.add(flip)
        # Update the maximum integer seen so far.
        max_seen = max(max_seen, flip)
        # If the size of the flipped set equals the maximum integer seen,
        # it means all bits up to max_seen are flipped, and the string is prefix-aligned.
        if len(flipped_set) == max_seen:
            count_aligned += 1
            
    return count_aligned