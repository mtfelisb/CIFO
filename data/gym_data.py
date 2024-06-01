valid_times = ['Morning', 'Afternoon', 'Evening']

gyms = {
    'Fitness24': {'capacity': {'Morning': 3, 'Afternoon': 2, 'Evening': 3}},
    'Crossfit Gym': {'capacity': {'Morning': 2, 'Afternoon': 2, 'Evening': 2}},
    'GymX': {'capacity': {'Morning': 3, 'Afternoon': 2, 'Evening': 3}},
    'StrongFit': {'capacity': {'Morning': 1, 'Afternoon': 1, 'Evening': 1}}
}

users = {
    'João': {'preference': {'time': 'Evening', 'gym': 'Fitness24'}},
    'Maria': {'preference': {'time': 'Evening', 'gym': 'Fitness24'}},
    'Cecília': {'preference': {'time': 'Evening', 'gym': 'Crossfit Gym'}},
    'Antonio': {'preference': {'time': 'Evening', 'gym': 'Crossfit Gym'}},
    'Julieta': {'preference': {'time': 'Evening', 'gym': 'Fitness24'}},
    'Pedro': {'preference': {'time': 'Evening', 'gym': 'GymX'}},
    'Ana': {'preference': {'time': 'Evening', 'gym': 'GymX'}},
    'Carlos': {'preference': {'time': 'Evening', 'gym': 'GymX'}},
    'Isabel': {'preference': {'time': 'Morning', 'gym': 'Fitness24'}},
    'Rafael': {'preference': {'time': 'Afternoon', 'gym': 'GymX'}},
    'Paula': {'preference': {'time': 'Morning', 'gym': 'Fitness24'}},
    'Bruno': {'preference': {'time': 'Afternoon', 'gym': 'GymX'}},
    'Luisa': {'preference': {'time': 'Evening', 'gym': 'Fitness24'}},
    'Ricardo': {'preference': {'time': 'Morning', 'gym': 'GymX'}}
}

distances = {
    'João': {'Fitness24': 1.2, 'Crossfit Gym': 3.0, 'GymX': 1.8, 'StrongFit': 2.0},
    'Maria': {'Fitness24': 1.0, 'Crossfit Gym': 2.8, 'GymX': 1.6, 'StrongFit': 1.9},
    'Cecília': {'Fitness24': 2.3, 'Crossfit Gym': 2.6, 'GymX': 2.2, 'StrongFit': 2.8},
    'Antonio': {'Fitness24': 3.2, 'Crossfit Gym': 1.0, 'GymX': 3.5, 'StrongFit': 2.5},
    'Julieta': {'Fitness24': 2.1, 'Crossfit Gym': 2.2, 'GymX': 1.9, 'StrongFit': 2.4},
    'Pedro': {'Fitness24': 2.5, 'Crossfit Gym': 1.7, 'GymX': 1.1, 'StrongFit': 1.8},
    'Ana': {'Fitness24': 2.8, 'Crossfit Gym': 2.6, 'GymX': 2.0, 'StrongFit': 1.2},
    'Carlos': {'Fitness24': 1.5, 'Crossfit Gym': 3.0, 'GymX': 1.0, 'StrongFit': 2.2},
    'Isabel': {'Fitness24': 3.1, 'Crossfit Gym': 2.9, 'GymX': 2.4, 'StrongFit': 2.6},
    'Rafael': {'Fitness24': 2.7, 'Crossfit Gym': 1.4, 'GymX': 2.1, 'StrongFit': 1.8},
    'Paula': {'Fitness24': 2.2, 'Crossfit Gym': 3.1, 'GymX': 1.5, 'StrongFit': 2.7},
    'Bruno': {'Fitness24': 2.9, 'Crossfit Gym': 1.8, 'GymX': 1.4, 'StrongFit': 2.3},
    'Luisa': {'Fitness24': 1.8, 'Crossfit Gym': 2.5, 'GymX': 2.3, 'StrongFit': 1.1},
    'Ricardo': {'Fitness24': 2.1, 'Crossfit Gym': 2.7, 'GymX': 1.2, 'StrongFit': 2.4}
}
