from random import sample, shuffle


def scramble_mutation(individual):
    """Scramble mutation for a GA individual.
    It works by selecting a subset segment, and then shuffle among them.

    Args:
        individual (Individual): A GA individual from Charles

    Returns:
        Individual: a mutated individual
    """
    start, end = sorted(sample(range(len(individual)), 2))
    subset = individual[start:end+1]
    shuffle(subset)
    individual[start:end+1] = subset

    return individual
