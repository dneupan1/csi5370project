def integerBreak(n: int) -> int:
    """
    This function returns the maximum product of a given integer n broken into the sum of k positive integers where k >= 2.
    
    :param n: int - The integer to be broken into the sum of k positive integers
    :return: int - The maximum product achievable
    """
    
    # Base case: If n is 2 or 3, the maximum product can be directly returned as special cases
    if n == 2:
        return 1  # 2 = 1 + 1, 1 * 1 = 1
    if n == 3:
        return 2  # 3 = 2 + 1, 2 * 1 = 2
    
    # Initialize product to 1
    product = 1
    
    # While n is greater than 4, we keep reducing n by 3 and multiplying the product by 3
    # This is because 3 is the optimal number to maximize the product
    while n > 4:
        product *= 3
        n -= 3
    
    # Multiply the remaining n to the product and return
    return product * n
