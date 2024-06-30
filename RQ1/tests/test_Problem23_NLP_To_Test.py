import pytest
from Problem23_GeneratedSolution import reorderDigits as originalDigits  # Assuming the function 'originalDigits' is defined in 'solution.py'

@pytest.mark.parametrize("input_string, expected_output", [
    # Example 1: Contains zero, one, two
    ("owoztneoer", "012"),
    # Example 2: Contains four, five
    ("fviefuro", "45"),
    # Edge case: Empty string
    ("", ""),
    # All digits represented
    ("zeroonetwothreefourfivesixseveneightnine", "0123456789"),
    # Digits in a random order
    ("ninetwoonezero", "0129"),
    # Digits with repetition
    ("oneone", "11"),
    # Long string with mixed characters
    ("gigteightxtsixhreezerosevenineightfiveourfneightwo", "0123456788"),
    # Only one kind of digit
    ("zerozerozero", "000"),
    # String with repeated complex pattern
    ("onetwothreefourfivetwothreefourfive", "123452345"),
    # Test string with maximum complexity
    ("sesvenineixegiththreefourwofiveevensevensixour", "2345677")
])
def test_originalDigits(input_string, expected_output):
    """
    Tests the originalDigits function with various strings to ensure it correctly extracts and orders digits from jumbled English words.

    This test function verifies:
    - The ability to correctly identify and count each unique digit from zero to nine represented in English.
    - Handling of strings with no digit representation, ensuring output is an empty string.
    - The capability to handle repeated numbers and complex mixed inputs efficiently.
    - Proper ordering of digits in ascending order regardless of their order in the input string.

    Args:
    input_string (str): The input string containing jumbled English words of digits.
    expected_output (str): The expected output string of digits in ascending numerical order.
    """
    assert originalDigits(input_string) == expected_output, f"Test failed for input='{input_string}'. Expected output='{expected_output}', got='{originalDigits(input_string)}'"
