import pytest
from Problem14_GeneratedSolution import getMaxRepetitions  # Adjust the import path as needed

@pytest.mark.parametrize("s1, n1, s2, n2, expected", [
    ("acb", 4, "ab", 2, 2),  # Basic scenario with repetitions
    ("acb", 1, "acb", 1, 1),  # s1 equals s2
    ("acb", 1, "abc", 1, 0),  # s2 cannot be formed from s1
    ("abcabcabc", 3, "abc", 1, 9),  # s1 contains s2 multiple times
    ("abacb", 6, "bcaa", 1, 3),  # Scenario with cycle
    ("a", 10000, "a", 1, 10000),  # Large repetition numbers
])
def test_get_max_repetitions(s1, n1, s2, n2, expected):
    """
    Test the getMaxRepetitions function with various scenarios.
    Each test case checks if the function correctly calculates the maximum number
    of repetitions of s2 that can be obtained from s1 repeated n1 times, such that
    the resulting sequence can be divided into n2 parts, each equal to s2.
    """
    assert getMaxRepetitions(s1, n1, s2, n2) == expected, f"Failed for {s1}, {n1}, {s2}, {n2}"

