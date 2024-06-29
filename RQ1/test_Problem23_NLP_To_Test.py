from collections import Counter

def originalDigits(s):
    """
    Reconstructs the digits from their scrambled English representation.
    
    Args:
    s (str): A string containing scrambled letters from English representations of digits.
    
    Returns:
    str: A string of digits in ascending order that were represented by the input string.
    
    Explanation:
    We use the unique characteristics of each number's representation in English to determine
    the frequency of each number. The approach is based on identifying unique letters or unique
    counts after certain numbers have been determined.
    """
    # Count of each character in the input string
    count = Counter(s)
    
    # Array to hold the count of each digit
    out = [0] * 10
    
    # Using unique letters for certain numbers to determine their counts
    out[0] = count['z']  # Zero
    out[2] = count['w']  # Two
    out[4] = count['u']  # Four
    out[6] = count['x']  # Six
    out[8] = count['g']  # Eight
    
    # Determining counts of other digits by subtracting counts of uniquely determined digits
    out[3] = count['h'] - out[8]  # Three (h is in eight)
    out[5] = count['f'] - out[4]  # Five (f is in four)
    out[7] = count['s'] - out[6]  # Seven (s is in six)
    
    # For one and nine, they need a check after the above are removed
    out[1] = count['o'] - out[0] - out[2] - out[4]
    out[9] = count['i'] - out[5] - out[6] - out[8]
    
    # Construct the output based on the counts of each digit
    result = ''.join(str(i) * out[i] for i in range(10))
    return result