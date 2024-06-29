def validIPAddress(queryIP: str) -> str:
    """
    Determines whether the given queryIP is a valid IPv4 or IPv6 address or neither.
    
    :param queryIP: String, the IP address to validate.
    :return: String, "IPv4" if queryIP is a valid IPv4 address, "IPv6" if it's a valid IPv6 address, or "Neither" otherwise.
    """
    
    def isIPv4(ip: str) -> bool:
        """
        Checks if the provided string is a valid IPv4 address.
        """
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit():
                return False
            if not 0 <= int(part) <= 255:
                return False
            if part[0] == '0' and len(part) != 1:
                return False
        return True

    def isIPv6(ip: str) -> bool:
        """
        Checks if the provided string is a valid IPv6 address.
        """
        parts = ip.split(':')
        if len(parts) != 8:
            return False
        for part in parts:
            if not 1 <= len(part) <= 4:
                return False
            if not all(c in '0123456789abcdefABCDEF' for c in part):
                return False
        return True

    # Main function logic to determine IP type
    if queryIP.count('.') == 3:
        return "IPv4" if isIPv4(queryIP) else "Neither"
    elif queryIP.count(':') == 7:
        return "IPv6" if isIPv6(queryIP) else "Neither"
    else:
        return "Neither"