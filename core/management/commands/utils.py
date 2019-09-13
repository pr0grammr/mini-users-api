from random import shuffle, randint


def get_random_values_from_list(lst):
    """
    returns list with random index values
    :param lst: list
    :return list
    """
    random_amount = randint(0, len(lst) - 1)
    indices = []

    shuffle(lst)

    for i in lst[:random_amount]:
        indices.append(i)

    return indices
