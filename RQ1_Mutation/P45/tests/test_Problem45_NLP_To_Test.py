import pytest
from Problem45_GeneratedSolution import findItinerary as reconstruct_itinerary  # Assuming the function is named 'reconstruct_itinerary' and resides in 'solution.py'

@pytest.mark.parametrize("tickets, expected", [
    ([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]], ["JFK", "MUC", "LHR", "SFO", "SJC"]),
    ([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]], ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]),
    ([["JFK", "LAX"], ["LAX", "JFK"]], ["JFK", "LAX", "JFK"]),  # Simple round trip
    ([["JFK", "ATL"], ["ATL", "JFK"], ["JFK", "ATL"], ["ATL", "JFK"]], ["JFK", "ATL", "JFK", "ATL", "JFK"]),  # Multiple possible paths, same route repeated
    ([["JFK", "LGA"], ["LGA", "ORD"], ["ORD", "ATL"], ["ATL", "JFK"]], ["JFK", "LGA", "ORD", "ATL", "JFK"]),  # Circular path
    #([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"], ["JFK", "ATL"]], ["JFK", "ATL", "JFK", "ATL", "SFO", "ATL", "JFK", "SFO"]),
    ([["JFK", "NRT"], ["NRT", "JFK"], ["JFK", "NRT"], ["NRT", "ATL"], ["ATL", "JFK"]], ["JFK", "NRT", "ATL", "JFK", "NRT", "JFK"]),  # Complex multi-route with backtracking
])
def test_reconstruct_itinerary(tickets, expected):
    """
    Tests the reconstruct_itinerary function with various configurations of airline tickets to ensure it correctly reconstructs the itinerary.

    This test function aims to:
    - Ensure the itinerary starts with "JFK" and uses all tickets exactly once.
    - Validate both simple direct trips and more complex scenarios with multiple valid itineraries and lexical ordering considerations.
    - Handle special cases like round trips, repeated routes, and itineraries requiring to sort multiple valid paths lexicographically.

    Args:
    tickets (list of list of str): List of airline tickets where each ticket is a pair [from, to].
    expected (list of str): Expected result of the reconstructed itinerary.
    """
    assert reconstruct_itinerary(tickets) == expected, f"Test failed for input {tickets}"
