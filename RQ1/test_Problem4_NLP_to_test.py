def isMatch(s: str, p: str) -> bool:
    """
    This function implements regular expression matching with support for '.' and '*'.
    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.

    :param s: Input string
    :param p: Pattern string
    :return: True if the pattern matches the entire input string, False otherwise
    """

    # Use a dynamic programming approach to solve the problem
    # dp[i][j] will be True if s[0..i-1] matches p[0..j-1], False otherwise
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    # Base case: empty string matches empty pattern
    dp[0][0] = True

    # Handle patterns with '*' where they can match zero preceding elements
    for j in range(2, len(dp[0])):
        dp[0][j] = dp[0][j-2] if p[j-1] == '*' else False

    # Fill the dp table
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if p[j-1] == '*':
                # '*' can match zero or more of the preceding element
                dp[i][j] = dp[i][j-2] or (dp[i-1][j] if (p[j-2] == s[i-1] or p[j-2] == '.') else False)
            else:
                # Match the current character or '.'
                dp[i][j] = dp[i-1][j-1] if (p[j-1] == s[i-1] or p[j-1] == '.') else False

    # The answer is in the bottom-right cell of the dp table
    return dp[len(s)][len(p)]