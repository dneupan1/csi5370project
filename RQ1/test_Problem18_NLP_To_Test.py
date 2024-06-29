def flipLights(n, presses):
    """
    Determines the number of unique configurations for n bulbs after a given number of button presses.

    :param n: Integer, number of bulbs in the room.
    :param presses: Integer, number of times the buttons can be pressed.
    :return: Integer, number of unique configurations possible.
    """
    # If no presses are made, the configuration remains as all bulbs on.
    if presses == 0:
        return 1

    # For simplicity and given constraints, reduce the problem space for n.
    if n == 1:
        # Only two outcomes are possible: all on or all off (via button 1)
        return 2
    elif n == 2:
        # If there are two bulbs, and we can press at least one button:
        if presses == 1:
            # After one press, three configurations are possible.
            return 3
        else:
            # If more than one press, all configurations can be achieved.
            return 4
    else:
        # For n >= 3, the number of unique configurations expands.
        if presses == 1:
            # With one press, 4 configurations are possible (one for each button).
            return 4
        elif presses == 2:
            # With two presses, 7 configurations are achievable.
            return 7
        else:
            # With three or more presses, all 8 configurations are achievable.
            return 8