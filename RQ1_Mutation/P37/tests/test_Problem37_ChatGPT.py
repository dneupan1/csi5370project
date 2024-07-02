# test file
import pytest
from Problem37_GeneratedSolution import maxEnvelopes  # Adjust this import based on your file structure

# Test with no envelopes
def test_no_envelopes():
    envelopes = []
    expected = 0
    assert maxEnvelopes(envelopes) == expected, "Failed with no envelopes"

# Test with envelopes that can all be nested
def test_all_nestable_envelopes():
    envelopes = [[1, 2], [2, 3], [3, 4]]
    expected = 3
    assert maxEnvelopes(envelopes) == expected, "Failed with all nestable envelopes"


# Test with envelopes having same width but different heights
def test_same_width_different_heights():
    envelopes = [[4, 5], [4, 6], [4, 7], [4, 4]]
    expected = 1  # Only one can be chosen because they have the same width
    assert maxEnvelopes(envelopes) == expected, "Failed with same width but different heights"

# Test with envelopes having same height but different widths
def test_different_widths_same_height():
    envelopes = [[5, 4], [6, 4], [7, 4]]
    expected = 1  # Only one can be chosen because sorting will place them adjacently with non-increasing heights
    assert maxEnvelopes(envelopes) == expected, "Failed with different widths but same height"

# Test with one envelope
def test_single_envelope():
    envelopes = [[1, 1]]
    expected = 1  # Only one envelope to choose
    assert maxEnvelopes(envelopes) == expected, "Failed with a single envelope"

# Test with reverse ordered envelopes that can all be nested
def test_reverse_ordered_nestable_envelopes():
    envelopes = [[3, 4], [2, 3], [1, 2]]
    expected = 3
    assert maxEnvelopes(envelopes) == expected, "Failed with reverse ordered nestable envelopes"
