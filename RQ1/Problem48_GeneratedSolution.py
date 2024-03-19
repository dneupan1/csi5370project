
def maxProduct(n):
    """
    Calculate the maximum product of the sum of positive integers that add up to n.
    
    The function uses a greedy approach to always try and split n into as many 3's as possible,
    with the remainder being handled specifically to maximize the product.
    
    Args:
    n: An integer representing the number to be split.
    
    Returns:
    An integer representing the maximum product achievable.
    """
    # Base cases
    if n == 2: return 1  # 2 can only be split into 1 + 1
    if n == 3: return 2  # 3 is best left as a single number rather than split into 1 + 2
    
    # The product variable is initialized to 1 to act as an accumulator.
    product = 1
    # While n is greater than 4, keep dividing it by 3 and multiply the product by 3.
    while n > 4:
        product *= 3
        n -= 3
    # Multiply the remainder, which will be in the range [2, 4], maximizing the last part of the product.
    product *= n
    
    return product

