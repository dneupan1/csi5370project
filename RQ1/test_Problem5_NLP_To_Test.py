def isMatch(s: str, p: str) -> bool:
    """
    This function implements wildcard pattern matching with support for '?' and '*'.
    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).

    :param s: Input string
    :param p: Pattern string
    :return: True if the pattern matches the entire input string, False otherwise
    """

    # Use a dynamic programming approach to solve the problem
    # dp[i][j] will be True if s[0..i-1] matches p[0..j-1], False otherwise
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    # Base case: empty string matches empty pattern
    dp[0][0] = True

    # Handle patterns with '*' where they can match any sequence (including empty)
    for j in range(1, len(p) + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-1]

    # Fill the dp table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j-1] == '*':
                # '*' can match any sequence: match zero or more characters
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
            elif p[j-1] == '?' or s[i-1] == p[j-1]:
                # '?' matches any single character or exact match of characters
                dp[i][j] = dp[i-1][j-1]

    # The answer is in the bottom-right cell of the dp table
    return dp[len(s)][len(p)]