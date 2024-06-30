import pytest
from Problem15_GeneratedSolution import validIPAddress  # Assuming the function 'validIPAddress' is defined in 'solution.py'

@pytest.mark.parametrize("queryIP, expected", [
    # Example 1: Valid IPv4 address
    ("172.16.254.1", "IPv4"),
    # Example 2: Valid IPv6 address
    ("2001:0db8:85a3:0:0:8A2E:0370:7334", "IPv6"),
    # Example 3: Neither IPv4 nor IPv6
    ("256.256.256.256", "Neither"),
    # Valid IPv4 address with leading zeros
    ("192.168.1.1", "IPv4"),
    # Invalid IPv4 address with leading zeros
    ("192.168.01.1", "Neither"),
    # Invalid IPv4 address with non-numeric characters
    ("192.168.1.00", "Neither"),
    # Valid IPv4 address at boundary
    ("0.0.0.0", "IPv4"),
    # Invalid IPv4 address out of range
    ("192.168.1.256", "Neither"),
    # Valid IPv6 address with different segments
    ("2001:db8:85a3:0:0:8A2E:0370:7334", "IPv6"),
    # Valid IPv6 address with leading zeros
    ("2001:0db8:85a3:0000:0000:8a2e:0370:7334", "IPv6"),
    # Invalid IPv6 address with non-hexadecimal character
    ("2001:0db8:85a3::8A2E:037j:7334", "Neither"),
    # Invalid IPv6 address with shorthand notation
    ("2001:0db8:85a3::8A2E:0370:7334", "Neither"),
    # Invalid IPv6 address with too many segments
    ("2001:0db8:85a3:0000:0000:8a2e:0370:7334:1234", "Neither"),
    # Valid IPv6 address with uppercase hexadecimal
    ("2001:DB8:85A3:0000:0000:8A2E:0370:7334", "IPv6"),
    # Valid IPv6 address with mixed case hexadecimal
    ("2001:Db8:85a3:0000:0000:8A2e:0370:7334", "IPv6"),
    # Valid IPv4 with boundary cases
    ("255.255.255.255", "IPv4"),
    # Invalid IPv4 address with extra segments
    ("192.168.1.1.1", "Neither"),
    # Valid IPv6 address with minimal segments
    #("::1", "IPv6"),
    # Edge case: Empty string
    ("", "Neither")
])
def test_validIPAddress(queryIP, expected):
    """
    Tests the validIPAddress function with various IP addresses to ensure it correctly classifies them as IPv4, IPv6, or Neither.

    This test function verifies:
    - Proper handling of valid and invalid IPv4 addresses, including boundary cases.
    - Proper handling of valid and invalid IPv6 addresses, including boundary cases and different notations.
    - Correct classification of IP addresses with non-numeric characters, leading zeros, and improper formats.
    - Edge cases such as empty strings.

    Args:
    queryIP (str): The input IP address string.
    expected (str): The expected result, either "IPv4", "IPv6", or "Neither".
    """
    result = validIPAddress(queryIP)
    assert result == expected, f"Test failed for queryIP='{queryIP}'. Expected {expected}, got {result}"
