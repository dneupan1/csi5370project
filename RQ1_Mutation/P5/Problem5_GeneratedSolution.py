def isMatch(s: str, p: str) -> bool:
    # Initialize DP table
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True

    # Handle '*' in the pattern matching empty sequence
    for j in range(1, len(p) + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-1]

    # Fill DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j-1] == '?':
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]

    return dp[len(s)][len(p)]
