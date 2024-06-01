from random import randint, random


def two_point_xo(parent1, parent2):
    """Implementation of two-point crossover.
    It works by creating a window (two-point) in the parents sequences,
    and then cross over the segments within the window in the offsprings.

    Args:
        parent1 (Individual): First parent for crossover
        parent2 (Individual): Second parent for crossover

    Returns:
        Individuals: Two offsprings resulting from the crossover.
    """
    size = len(parent1)
    point1 = randint(1, size - 2)
    point2 = randint(point1, size - 1)

    offspring1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    offspring2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]

    return offspring1, offspring2


def uniform_xo(parent1, parent2):
    """Implementation of uniform crossover
    It works by crossing over half of segments at random order.

    Args:
        parent1 (Individual): First parent for crossover
        parent2 (Individual): Second parent for crossover

    Returns:
        Individuals: Two offsprings resulting from the crossover.
    """
    offspring1, offspring2 = parent1[:], parent2[:]

    for i in range(len(parent1)):
        if random() < 0.5:
            offspring1[i], offspring2[i] = parent1[i], parent2[i]

    return offspring1, offspring2
