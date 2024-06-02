import argparse


def get_args():
    """Function to read from sys args
    and convert into a typed dict

    Returns:
        Namespace: all typed parameters
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--runs', dest='runs', type=int, help='Add runs')
    parser.add_argument('--gens', dest='gens', type=int, help='Add gens')
    parser.add_argument('--pop_size', dest='pop_size', type=int, help='Add pop_size')
    parser.add_argument('--elitism', dest='elitism', type=bool, help='Add elitism')
    parser.add_argument('--save_to', dest='save_to', type=str, help='Add save_to')

    return parser.parse_args()

