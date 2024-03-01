def validIPAddress(self, queryIP: str) -> str:
    def is_valid_ipv4(s):
        try:
            return str(int(s)) == s and 0 <= int(s) <= 255
        except:
            return False

    def is_valid_ipv6(s):
        if len(s) > 4:
            return False
        try:
            int(s, 16)
            return True
        except:
            return False
    
    if queryIP.count('.') == 3 and all(is_valid_ipv4(i) for i in queryIP.split('.')):
        return "IPv4"
    elif queryIP.count(':') == 7 and all(is_valid_ipv6(i) for i in queryIP.split(':')):
        return "IPv6"
    else:
        return "Neither"