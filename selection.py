from operator import attrgetter
import numpy as np


def ranking_sel(population):
    """Ranking selection implementation.

    Args:
        population (Population): The population we want to select from.

    Returns:
        Individual: selected individual.
    """

    sorted_pop = sorted(population, key=attrgetter("fitness"))
    ranking = range(1, len(sorted_pop) + 1)
    total_ranking = sum(ranking)
    selection_probs = [position / total_ranking for position in ranking]
    selected_index = np.random.choice(len(population), p=selection_probs)

    return sorted_pop[selected_index]
