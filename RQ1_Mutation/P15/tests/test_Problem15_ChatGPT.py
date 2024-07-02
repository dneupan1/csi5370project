import pytest
from Problem15_GeneratedSolution import validIPAddress  # Adjust the import path as needed

@pytest.mark.parametrize("queryIP, expected", [
    # IPv4 tests
    ("192.168.1.1", "IPv4"),
    ("255.255.255.255", "IPv4"),
    ("0.0.0.0", "IPv4"),
    ("256.256.256.256", "Neither"),  # Value out of range
    ("192.168.1.01", "Neither"),  # Leading zero
    ("192.168.1", "Neither"),  # Not enough segments
    ("192.168.1.256", "Neither"),  # Value out of range
    
    # IPv6 tests
    ("2001:0db8:85a3:0000:0000:8a2e:0370:7334", "IPv6"),
    ("FE80:0000:0000:0000:0202:B3FF:FE1E:8329", "IPv6"),
    ("2001:db8:85a3:0:0:8A2E:0370:7334", "IPv6"),  # Mixed case
    ("2001:0db8:85a3::8a2e:0370:7334", "Neither"),  # Double colons
    ("2001:0db8:85a3:0000:0000:8a2e:0370:733z", "Neither"),  # Invalid character
    
    # Neither
    ("192.168.1.1.1", "Neither"),  # Too many segments for IPv4
    ("2001:0db8:85a3:0000:0000:8a2e:0370:7334:1234", "Neither"),  # Too many segments for IPv6
    ("abc", "Neither"),  # Clearly neither
    ("", "Neither"),  # Empty string
])
def test_valid_ip_address(queryIP, expected):
    """
    Tests the validIPAddress function with various IP addresses and expected outcomes.
    """
    assert validIPAddress(queryIP) == expected, f"Failed for IP: {queryIP}"