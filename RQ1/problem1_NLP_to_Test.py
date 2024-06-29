import pytest
from Problem1_GeneratedSolution import length_of_longest_substring

def test_basic_example():
    """
    Test the basic example provided in the problem statement.
    """
    assert length_of_longest_substring("abcabcbb") == 3

def test_single_character_string():
    """
    Test with a string of identical characters.
    This helps ensure that the function handles cases where all characters are the same.
    """
    assert length_of_longest_substring("bbbbb") == 1

def test_string_with_mixed_repeats():
    """
    Test a more complex case with mixed repeated characters.
    """
    assert length_of_longest_substring("pwwkew") == 3

def test_empty_string():
    """
    Test the edge case with an empty string.
    This is important for ensuring that the function handles minimal input gracefully.
    """
    assert length_of_longest_substring("") == 0

def test_no_repeats():
    """
    Test a string with no repeated characters at all.
    """
    assert length_of_longest_substring("abcdef") == 6

def test_long_string_with_repeats():
    """
    Test with a longer string to check efficiency and correctness over larger input.
    """
    input_string = "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
    assert length_of_longest_substring(input_string) == 4

def test_string_with_non_alphabet_characters():
    """
    Test strings that include digits and special characters to ensure robustness with non-alphabet inputs.
    """
    assert length_of_longest_substring("a1!a1!a1!") == 3

def test_unicode_characters():
    """
    Test strings that include Unicode characters to ensure the function handles different character sets.
    """
    assert length_of_longest_substring("你好你好") == 2

# Optionally, you might want to test the function's performance with very long strings.
@pytest.mark.performance
def test_performance():
    """
    Performance test for very long strings.
    This test is marked for performance to differentiate it from standard unit tests.
    """
    import time
    start_time = time.time()
    assert length_of_longest_substring("a" * 10000 + "b" * 10000) == 2
    end_time = time.time()
    assert end_time - start_time < 1  # The test should run in less than one second

