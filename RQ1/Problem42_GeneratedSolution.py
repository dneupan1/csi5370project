def mergeStones(stones, k):
    n = len(stones)
    if (n - 1) % (k - 1) != 0:
        return -1  # Impossible to merge into one pile

    # Precompute prefix sums for quick range sum calculation
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + stones[i]

    # Initialize DP table with a large integer value
    dp = [[10**9] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0  # Cost to merge pile with itself is 0

    # Fill DP table
    for length in range(2, n + 1):  # Start with subarrays of length 2
        for left in range(n - length + 1):
            right = left + length - 1
            # Calculate cost to merge subarray [left:right+1]
            for mid in range(left, right, k - 1):
                # Only try to split where possible
                dp[left][right] = min(dp[left][right], dp[left][mid] + dp[mid + 1][right])
            if (right - left) % (k - 1) == 0:
                dp[left][right] += prefix_sum[right + 1] - prefix_sum[left]

    # Check if we have updated our answer from the initial value
    return dp[0][n - 1] if dp[0][n - 1] < 10**9 else -1


