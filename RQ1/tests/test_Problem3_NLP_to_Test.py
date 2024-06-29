def reverse(x: int) -> int:
    """
    This function takes a signed 32-bit integer x and returns x with its digits reversed.
    If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1],
    then it returns 0.

    :param x: Signed 32-bit integer
    :return: Reversed integer or 0 if the result is out of bounds
    """

    # Define the 32-bit integer boundaries
    INT_MIN, INT_MAX = -2**31, 2**31 - 1

    # Store the sign of the number and work with its absolute value
    sign = -1 if x < 0 else 1
    x = abs(x)

    # Initialize the reversed number to 0
    reversed_num = 0

    # Process each digit in the integer
    while x != 0:
        # Get the last digit of the number
        digit = x % 10
        x //= 10  # Remove the last digit from the number

        # Check for overflow before updating the reversed number
        if reversed_num > (INT_MAX - digit) // 10:
            return 0

        # Update the reversed number
        reversed_num = reversed_num * 10 + digit

    # Apply the original sign to the reversed number
    reversed_num *= sign

    # Return the reversed number
    return reversed_num