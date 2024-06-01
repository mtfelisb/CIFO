import itertools
from tqdm import tqdm
import pandas as pd

from charles.charles import Individual, Population
from charles.mutation import swap_mutation, inversion_mutation
from charles.selection import tournament_sel, fps
from charles.xo import single_point_xo

from fitness import get_fitness
from representation import get_genotype
from data.gym_data import gyms_keys, valid_times, users
from xo import two_point_xo, uniform_xo
from selection import ranking_sel
from mutation import scramble_mutation

# monkey patching
Individual.get_fitness = get_fitness

# creates the valid set
valid_set = [get_genotype(gym, time) for gym in gyms_keys for time in valid_times]


def run(combination, total=20, gens=20, pop_size=20, elitism=True):
    """Runs a configuration with a defined genetic operator combination.

    Args:
        combination: contains the selection, mutation, and xo methods
        total: the number of times to run the genetic algorithm
        gens: the number of generations
        pop_size: the number of population size
        elitism: a boolean indicating if elitism should be used

    Returns:
        DataFrame: a dataframe with the median fitness score over all generations
    """
    run_result = pd.DataFrame()

    for i in range(total):
        pop = Population(size=pop_size, optim="max", sol_size=len(users), valid_set=valid_set, repetition=True)
        best_fitness_scores = pop.evolve(
            gens=gens,
            xo_prob=0.9,
            mut_prob=0.15,
            select=selection_methods[combination["select"]],
            xo=crossover_methods[combination["xo"]],
            mutate=mutation_methods[combination["mutate"]],
            elitism=elitism,
        )

        run_result[i] = [f.get_fitness() for f in best_fitness_scores]

    # median over mean to be more robust against outliers
    return run_result.median(axis=1)


# a dictionary with all genetic operators
selection_methods = {"ranking_sel": ranking_sel, "tournament_sel": tournament_sel, "fps": fps}
crossover_methods = {"two_point_xo": two_point_xo, "single_point_xo": single_point_xo, "uniform_xo": uniform_xo}
mutation_methods = {"swap_mutation": swap_mutation, "inversion_mutation": inversion_mutation, "scramble_mutation": scramble_mutation}

# creates an exhaustive list of all combinations between genetic operators
combinations = list(itertools.product(selection_methods.keys(),
                                      crossover_methods.keys(), mutation_methods.keys()))

# prepare the solutions based on the combinations
solutions = []
for idx, (select, xo, mutate) in enumerate(combinations, start=1):
    solution = {
        "id": f"#{idx}",
        "select": select,
        "xo": xo,
        "mutate": mutate
    }
    solutions.append(solution)

results = pd.DataFrame()
for solution in tqdm(range(len(solutions))):
    results[solutions[solution]["id"]] = run(solutions[solution], 100, 100, 40, False)

# saving the results to be further analyzed
results.to_csv("./results/100-100-40-F.csv")

# saving the solutions combinations to be further explored
pd.DataFrame(solutions).to_csv("./results/solutions.csv")
