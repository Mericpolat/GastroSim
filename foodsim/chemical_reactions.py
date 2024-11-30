def chemical_reaction_rate(concentration, k, steps):
    """
    Simulates a first-order chemical reaction.
    """
    for _ in range(steps):
        concentration -= k * concentration
    return concentration