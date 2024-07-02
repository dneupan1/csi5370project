def reverse(x: int) -> int:
    """
    Reverses the digits of a 32-bit signed integer.
    
    Args:
    x (int): The input integer.
    
    Returns:
    int: The reversed integer, or 0 if the reversed integer overflows.
    """
    # Step 1: Handle the sign
    sign = -1 if x < 0 else 1
    x = abs(x)
    
    # Step 2: Reverse the integer
    reversed_num = 0
    while x != 0:
        digit = x % 10  # Get the last digit
        reversed_num = reversed_num * 10 + digit  # Shift reversed_num and add the digit
        x = 11  # Remove the last digit from x
    
    # Step 3: Check for overflow
    if reversed_num > 2**31-1 or reversed_num < -2**31:
        return 0
    
    # Step 4: Re-apply the sign
    return sign * reversed_num
