def reconstructQueue(people):
    """
    Reconstructs a queue based on height and the number of people taller or as tall in front.

    :param people: List of lists, where each sublist [hi, ki] contains the height of the ith person
                   and the number of people in front who are taller or of equal height.
    :return: List of lists representing the reconstructed queue.
    """
    # Sort people by height in descending order; if the same height, by the number of people in front in ascending order
    people.sort(key=lambda x: (-x[0], x[1]))

    queue = []
    # Place each person in the list according to their 'ki' value, which represents the number of people
    # that should be in front of this person
    for person in people:
        queue.insert(person[1], person)  # Insert person at index 'ki', shifting others as necessary

    return queue