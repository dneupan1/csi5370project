def getMaxRepetitions(s1, n1, s2, n2):
    # Early exit if s2 cannot be formed from s1
    if set(s2) - set(s1):
        return 0

    # Counters for occurrences of s2 in s1, and repetitions of s1
    s1_count, s2_count = 0, 0
    index_s2 = 0
    s2_length, s1_length = len(s2), len(s1)

    # Map to remember the state of each cycle
    seen = {}
    while True:
        s1_count += 1
        # Traverse s1 to match characters in s2
        for char in s1:
            if char == s2[index_s2]:
                index_s2 += 1
                if index_s2 == s2_length:  # Found s2 in s1
                    index_s2 = 0
                    s2_count += 1
        # If we completed all n1 repetitions of s1
        if s1_count == n1:
            return s2_count // n2

        # Cycle detection: if we see a repeated state, we found a cycle
        if index_s2 in seen:
            s1_count_prev, s2_count_prev = seen[index_s2]
            # Pre-cycle length and counts
            pre_cycle_s1_count = s1_count_prev
            pre_cycle_s2_count = s2_count_prev
            # Cycle length and counts
            cycle_s1_count = s1_count - s1_count_prev
            cycle_s2_count = s2_count - s2_count_prev

            # How many full cycles can we execute with the remaining s1 repetitions?
            full_cycles = (n1 - pre_cycle_s1_count) // cycle_s1_count

            # Total s2 count is from pre-cycle + full cycles * cycle_s2_count
            total_s2_count = pre_cycle_s2_count + full_cycles * cycle_s2_count

            # Remaining s1 repetitions after accounting for full cycles
            remaining_s1_count = (n1 - pre_cycle_s1_count) % cycle_s1_count

            # Add the s2 count achievable with the remaining s1 repetitions
            for _ in range(remaining_s1_count):
                for char in s1:
                    if char == s2[index_s2]:
                        index_s2 += 1
                        if index_s2 == s2_length:
                            index_s2 = 0
                            total_s2_count += 1
            # Return the total s2 count found divided by n2
            return total_s2_count // n2
        else:
            # Remember the state for cycle detection
            seen[index_s2] = (s1_count, s2_count)