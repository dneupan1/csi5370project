
from collections import defaultdict

def findItinerary(tickets):
    # Create a graph where each airport points to a list of airports it can fly to
    graph = defaultdict(list)
    for src, dst in sorted(tickets, reverse=True):
        graph[src].append(dst)

    route = []
    def visit(airport):
        # While there are airports to visit from the current airport, visit them
        while graph[airport]:
            # Pop the last destination from the airport's destination list to maintain lexical order
            next_airport = graph[airport].pop()
            visit(next_airport)
        route.append(airport)
    
    visit('JFK') # Start the journey from JFK
    return route[::-1] # Return the route in the correct order

