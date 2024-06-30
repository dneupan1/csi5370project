import pytest
from Problem14_GeneratedSolution import getMaxRepetitions  # Assuming the function 'getMaxRepetitions' is defined in 'solution.py'

@pytest.mark.parametrize("s1, n1, s2, n2, expected", [
    # Example 1: Basic example with s1 and s2 having different characters
    ("acb", 4, "ab", 2, 2),
    # Example 2: Basic example with s1 and s2 being identical
    ("acb", 1, "acb", 1, 1),
    # No possible subsequence of s2 in s1
    ("abc", 2, "def", 2, 0),
    # s1 repeated many times can match s2 repeated fewer times
    ("abc", 10, "ab", 5, 5),
    # Edge case: Single character repeated many times
    ("a", 1000, "aa", 1, 500),
    # Edge case: s1 and s2 are the same but n2 is larger than n1
    ("abc", 1, "abc", 2, 0),
    # Complex case with interleaved characters
    ("abacb", 5, "ab", 3, 3),
    # Long strings with repeated patterns
    ("abcabcabc", 3, "abc", 3, 3),
    # Edge case: Large n1 and n2 values
    ("abc", 100, "a", 50, 200),
    # Test with no repeats (n1 and n2 are 1)
    ("acb", 1, "ab", 1, 1),
])
def test_getMaxRepetitions(s1, n1, s2, n2, expected):
    """
    Tests the getMaxRepetitions function with various inputs to ensure it correctly determines the maximum number of times
    str2 can be obtained from str1.

    This test function verifies:
    - Proper handling of basic examples provided in the problem description.
    - Edge cases such as no possible subsequences, single character strings, and large values of n1 and n2.
    - Correct computation for complex cases with interleaved characters and long strings.

    Args:
    s1 (str): The first string.
    n1 (int): The number of times s1 is repeated.
    s2 (str): The second string.
    n2 (int): The number of times s2 is repeated.
    expected (int): The expected maximum number of times str2 can be obtained from str1.
    """
    result = getMaxRepetitions(s1, n1, s2, n2)
    assert result == expected, f"Test failed for s1={s1}, n1={n1}, s2={s2}, n2={n2}. Expected {expected}, got {result}"
