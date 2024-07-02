def flipLights(n, presses):
    # When no press is made or no bulbs exist, the number of configurations is 1.
    if presses == 0 or n == 0:
        return 1
    
    # For one bulb, there are two possible states regardless of the number of presses.
    if n == 1:
        return 2
    
    # For two bulbs, there are three configurations if pressed once, and four if pressed more than once.
    if n == 2:
        return 3 if presses == 1 else 4
    
    # For three or more bulbs, we can derive configurations based on button press patterns.
    if presses == 1:
        return 4
    elif presses == 2:
        return 7
    else:
        return 8