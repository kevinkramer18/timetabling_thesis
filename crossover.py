import random


def crossover_process(topParent, bottomParent, child):
    rand = random.randint(0, len(topParent.offerings) - 1)

    return child