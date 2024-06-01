from data.gym_data import gyms_keys, users_keys, gyms, users, distances
from representation import get_phenotype

# used to balance how much distance is relevant
distance_weight = 0.5

# used to penalize extra capacities
capacity_penalty_weight = 10

# used to avoid negative scores
shift_constant = ((capacity_penalty_weight * len(users)) +
                  (distance_weight * max(max(d.values()) for d in distances.values())))


def get_fitness(individual):
    """A fitness function that implements the custom
    heuristic based on the fitness center capacity, and
    user preferences of time

    Args:
        individual: the individual to have a score calculated

    Returns:
        int: Fitness value
    """
    extra_capacity = 0
    preference_score = 0
    distance_penalty = 0

    gyms_loads = {gym: {"Morning": 0, "Afternoon": 0, "Evening": 0} for gym in gyms_keys}

    for user_id, solution in enumerate(individual.representation):
        user_key = users_keys[user_id]
        gym, time = get_phenotype(solution)
        gyms_loads[gym][time] += 1

        # penalizes if exceeds the gym capacity in the given time period
        if gyms_loads[gym][time] > gyms[gym]["capacity"][time]:
            extra_capacity += 1

        # rewards if meets user preference
        if time == users[user_key]["preference"]["time"]:
            preference_score += 1

        # increases the penalty accordingly with the distance
        distance_penalty += distances[user_key][gym]

    # fitness score formula
    fitness_score = preference_score - (extra_capacity * capacity_penalty_weight) - (distance_weight * distance_penalty)

    return fitness_score + shift_constant
