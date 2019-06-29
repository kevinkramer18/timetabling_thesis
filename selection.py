import random
import copy
from evaluation import fitness_function_1
from evaluation import fitness_function_3
from evaluation import fitness_function_2

def tournament_selection(population):
    randA = random.randint(0, len(population) - 1)
    timetableA = copy.deepcopy(population[randA])

    randB = randA

    while randB == randA:
        randB = random.randint(0, len(population) - 1)

    timetableB = copy.deepcopy(population[randB])

    scoreA = fitness_function_2(timetableA.faculty)
    scoreB = fitness_function_2(timetableB.faculty)

    if scoreA < scoreB:
        return randA
    elif scoreB <= scoreA:
        return randB


    #Returns num of parent & parent