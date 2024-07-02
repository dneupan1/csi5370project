def reconstructQueue(people):
    # Step 1: Sort the people
    # Sort by height in descending order, and by k value in ascending order
    people.sort(key=lambda x: (-x[0], x[1]))
    
    # Step 2: Place people in the queue
    queue = []
    for p in people:
        # Insert each person at the index equal to their k value
        queue.insert(p[1], p)
    
    return queue
