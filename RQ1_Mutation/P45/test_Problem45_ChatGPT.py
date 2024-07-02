# test file
import pytest
from Problem45_GeneratedSolution import findItinerary  # Adjust this import based on your file structure

# Test with a straightforward path
def test_straightforward_path():
    """
    Tests a scenario where there is a direct path with no branching.
    """
    tickets = [["JFK", "ATL"], ["ATL", "SFO"]]
    expected = ["JFK", "ATL", "SFO"]
    assert findItinerary(tickets) == expected, "Failed with a straightforward path"

# Test with multiple valid itineraries, lexical order decides
def test_lexical_order():
    """
    Tests cases with multiple valid paths where the itinerary should follow lexical order.
    """
    tickets = [["JFK", "ATL"], ["ATL", "JFK"], ["JFK", "ATL"], ["ATL", "SFO"]]
    expected = ["JFK", "ATL", "JFK", "ATL", "SFO"]
    assert findItinerary(tickets) == expected, "Failed with multiple valid itineraries"

# Test with complex route requiring backtracking
def test_complex_route_with_backtracking():
    """
    Tests a more complex scenario where the path requires backtracking.
    """
    tickets = [["JFK", "SFO"], ["SFO", "ATL"], ["ATL", "JFK"], ["JFK", "ATL"], ["ATL", "SFO"]]
    expected = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
    assert findItinerary(tickets) == expected, "Failed with a complex route requiring backtracking"

# Test with a single ticket
def test_single_ticket():
    """
    Tests a scenario with only one ticket.
    """
    tickets = [["JFK", "SFO"]]
    expected = ["JFK", "SFO"]
    assert findItinerary(tickets) == expected, "Failed with a single ticket"

# Test with no tickets
def test_no_tickets():
    """
    Tests the scenario where no tickets are available.
    """
    tickets = []
    expected = ["JFK"]  # The journey would start at JFK but immediately end due to no available tickets
    assert findItinerary(tickets) == expected, "Failed with no tickets"

# Test with cycles in the itinerary
def test_with_cycles():
    """
    Tests a scenario with cycles in the itinerary, requiring the algorithm to handle revisits gracefully.
    """
    tickets = [["JFK", "ATL"], ["ATL", "JFK"], ["JFK", "ATL"], ["ATL", "SFO"], ["SFO", "JFK"]]
    expected = ["JFK", "ATL", "JFK", "ATL", "SFO", "JFK"]
    assert findItinerary(tickets) == expected, "Failed with cycles in the itinerary"
