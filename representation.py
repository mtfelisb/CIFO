from data.gym_data import gyms, valid_times, gyms_keys


def get_genotype(gym, time):
    """Implements the encode function.
    It encodes the combination of gym and time using binary format,
    where 2 bits are used to represent a gym, and 2 bits to represent the time.

    Args:
        gym: a gym present in the dataset
        time: a time of the day

    Returns:
        Binary: the combination pair in binary format
    """
    gym_index = gyms_keys.index(gym)
    time_index = valid_times.index(time)

    return format(gym_index, "02b") + format(time_index, "02b")


def get_phenotype(binary):
    """Implements the decode function.
    It decodes the pair of gym and time from binary to int,
    that represents the index in the data.

    Args:
        binary: an encoded solution

    Returns:
        String, String: gym and time
    """
    gym_index = int(binary[:2], 2)
    time_index = int(binary[2:], 2)

    return gyms_keys[gym_index], valid_times[time_index]


def get_genotype_v2(gym, time):
    """Implements the encode function.
    It encodes the combination of gym and time as a pair of integers.

    Args:
        gym: a gym present in the dataset
        time: a time of the day

    Returns:
        Int, Int: the combination pair
    """
    gym_index = gyms_keys.index(gym)
    time_index = valid_times.index(time)

    return [gym_index, time_index]


def get_phenotype_v2(pair):
    """Implements the decode function.
    It decodes the pair of gym and time to int,
    that represents the index in the data.

    Args:
        Int, Int: an encoded solution

    Returns:
        String, String: gym and time
    """
    gym_index = pair[0]
    time_index = pair[1]

    return gyms_keys[gym_index], valid_times[time_index]
