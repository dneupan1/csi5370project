import pytest
from Problem19_GeneratedSolution import countPrefixAligned as numTimesPrefixAligned  # Assuming the function 'numTimesPrefixAligned' is defined in 'solution.py'

@pytest.mark.parametrize("flips, expected", [
    # Example 1: Prefix-aligned two times
    ([3, 2, 4, 1, 5], 2),
    # Example 2: Prefix-aligned one time
    ([4, 1, 2, 3], 1),
    # Single flip, always prefix-aligned
    ([1], 1),
    # Two flips, always prefix-aligned after second flip
    ([2, 1], 1),
    # Flip sequence that aligns after every flip
    ([1, 2, 3, 4, 5], 5),
    # No flips, never prefix-aligned
    ([], 0),
    # Flip sequence that never aligns
    ([5, 4, 3, 2, 1], 0),
    # Large sequence with only one alignment at the end
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 1),
    # Sequence with multiple prefix alignments in the middle
    ([2, 3, 4, 1, 5], 2),
    # Random flips with multiple alignments
    ([3, 1, 2, 5, 4], 3)
])
def test_numTimesPrefixAligned(flips, expected):
    """
    Tests the numTimesPrefixAligned function with various flip sequences to ensure it correctly counts the number of times the binary string becomes prefix-aligned.

    This test function verifies:
    - Proper handling of different flip sequences and their lengths.
    - Edge cases such as empty flip sequences and sequences that never align.
    - Multiple alignments and proper counting of those alignments.

    Args:
    flips (list of int): The sequence of flips applied to the binary string.
    expected (int): The expected number of times the binary string becomes prefix-aligned.
    """
    result = numTimesPrefixAligned(flips)
    assert result == expected, f"Test failed for flips={flips}. Expected {expected}, got {result}"
