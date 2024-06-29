from typing import List
from collections import defaultdict, deque

def findItinerary(tickets: List[List[str]]) -> List[str]:
    """
    This function returns the itinerary that uses all the given tickets exactly once
    and starts at 'JFK'. If there are multiple valid itineraries, it returns the one
    with the smallest lexical order.
    
    :param tickets: List[List[str]] - List of tickets where each ticket is a [from, to] pair
    :return: List[str] - The reconstructed itinerary
    """
    
    # Graph to store the flights as adjacency list with lexical order
    flight_map = defaultdict(deque)
    
    # Sort tickets to ensure lexical order and build the graph
    for from_city, to_city in sorted(tickets):
        flight_map[from_city].append(to_city)
    
    # List to store the final itinerary
    itinerary = []
    
    def visit(airport: str):
        # Use stack to avoid recursion limit in case of deep recursion
        stack = [airport]
        while stack:
            while flight_map[stack[-1]]:
                next_airport = flight_map[stack[-1]].popleft()
                stack.append(next_airport)
            itinerary.append(stack.pop())
    
    # Start the DFS from 'JFK'
    visit('JFK')
    
    # The itinerary is constructed in reverse order, so we need to reverse it before returning
    return itinerary[::-1]