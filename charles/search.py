from random import choice, uniform
from math import exp


def hill_climb(search_space):
    """Hill climbs a given search space.

    Args:
        search_space (Population): A Population of solutions

    Returns:
        Individual: Local optima Individual found in the search.
    """

    # initialize a feasible solution from search space
    start = choice(search_space)
    # current solution is i-start
    position = start
    iter_plateau = 0

    print(f"Initial position: {start}")
    # repeat
    while True:

        if iter_plateau > 5:
            print(f"Stuck at a plateau, returned {position}")
            return position

        # generate solution from neighbours
        n = position.get_neighbours()
        # fitness of the neighbours
        n_fit = [i.fitness for i in n]

        if search_space.optim == "max":
            best_n = n[n_fit.index(max(n_fit))]
            # if neighbour is better than current solution
            if best_n.fitness > position.fitness:
                print(f"Found better solution: {best_n}")
                # neighbour is the new solution
                position = best_n
                iter_plateau = 0
            elif best_n.fitness == position.fitness:
                print(f"Found better solution: {best_n}")
                # neighbour is the new solution
                position = best_n
                iter_plateau += 1
            else:
                # no better neighbour found
                print(f"HC found: {position}")
                return position

        elif search_space.optim == "min":
            best_n = n[n_fit.index(min(n_fit))]
            # if neighbour is better than current solution
            if best_n.fitness < position.fitness:
                print(f"Found better solution: {best_n}")
                # neighbour is the new solution
                position = best_n
                iter_plateau = 0
            elif best_n.fitness == position.fitness:
                print(f"Found better solution: {best_n}")
                # neighbour is the new solution
                position = best_n
                iter_plateau += 1
            else:
                # no better neighbour found
                print(f"HC found: {position}")
                return position


def sim_annealing(search_space, L=20, c=10, alpha=0.95, threshold=0.05):
    """Simulated annealing implementation.

    Args:
        search_space (Population): a Population object to search through.
        L (int, optional): Internal loop parameter. Defaults to 20.
        c (int, optional): Temperature parameter. Defaults to 10.
        alpha (float, optional): Alpha to decrease the temperature. Defaults to 0.95.

    Returns:
        Individual: an Individual object - the best found by SA.
    """
    # 1. random init
    position = choice(search_space)
    elite = position
    # 2. L and c init as inputs
    # 3. repeat until termination condition
    while c > threshold:
        # 3.1 repeat L times
        for _ in range(L):
            # 3.1.1 get random neighbour
            neighbour = choice(position.get_neighbours())

            if search_space.optim == "max":
                # 3.1.2 if neighbour fitness is better or equal, accept
                if neighbour.fitness >= position.fitness:
                    position = neighbour
                    print(f"Found better solution {position}")
                    if position.fitness >= elite.fitness:
                        elite = position
                # accept with a probability
                else:
                    # p: probability of accepting a worse solution
                    p = exp(-abs(neighbour.fitness-position.fitness)/c)
                    x = uniform(0, 1)
                    if p > x:
                        position = neighbour
                        print(f"Accepted a worse solution {position}")

            elif search_space.optim == "min":
                # 3.1.2 if neighbour fitness is better or equal, accept
                if neighbour.fitness <= position.fitness:
                    position = neighbour
                    print(f"Found better solution {position}")
                    if position.fitness <= elite.fitness:
                        elite = position
                # accept with a probability
                else:
                    # p: probability of accepting a worse solution
                    p = exp(-abs(neighbour.fitness-position.fitness)/c)
                    x = uniform(0, 1)
                    if p > x:
                        position = neighbour
                        print(f"Accepted a worse solution {position}")


        # 3.3 decrement c
        c = c * alpha
    # 4. return the best solution
    print(f"SA found {position}")
    print(f"SA with elitism found {elite}")
    return elite


