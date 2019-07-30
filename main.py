# Import Classes
from professor import Professor
from course import Course
from offering import Offering
from timeslot import Timeslot
from generalcourse import GeneralCourse
from section import Section
from timetable import Timetable

# Import Functions from Loading
from loading import load_course_list
from loading import load_faculty_list
from loading import load_offering_list
from loading import load_timeslot_list
from loading import load_general_course_list
from loading import load_section_list

from evaluation import fitness_function_1

from evaluation import fitness_function_2

from output import output_faculty_csv
from output import output_timetable_csv
from output import output_timeslots_csv

# Import Functions from Initialization
from initialization import initialize
import copy

# Import Functions from Selection
from selection import  tournament_selection

# Import Functions from Crossover
from crossover import crossover_process

# Import Time
import time

# List declarations
course_list = copy.deepcopy(list(load_course_list()))
faculty_list = copy.deepcopy(list(load_faculty_list()))
offering_list = copy.deepcopy(list(load_offering_list()))
timeslot_list = copy.deepcopy(list(load_timeslot_list()))
general_course_list = copy.deepcopy(list(load_general_course_list()))
section_list = copy.deepcopy(list(load_section_list()))


present_faculty_courses = []
pfc_count = 0
population = []

startTime = time.time()

# Removes offerings that are in excess of the faculty' total load limit and transfers them to a new list
unassigned_offering_list = []
total_offering_units  = 0.0
total_remaining_units = 0.0

total_faculty_load = 0.0

for item in faculty_list:
    total_faculty_load += item.load

for item in offering_list:
    total_offering_units += item.units

total_remaining_units = total_offering_units

while total_remaining_units > total_faculty_load:
    total_remaining_units -= offering_list[len(offering_list)-1].units
    del offering_list[len(offering_list)-1]

print("Total number of units:" + str(total_offering_units))
print("Total number of remaining units:" + str(total_remaining_units))


# Removing preferred courses that aren't present in the current set of offerings
for item in offering_list:
    present_faculty_courses.append(item.course_id)
present_faculty_courses = copy.deepcopy(list(set(present_faculty_courses)))
present_faculty_courses.sort()
temp_faculty_course = []
print("----------------------")
print(present_faculty_courses)
print("----------------------")

for item in faculty_list:
    print(item.first_name, item.last_name)
    item.preferred_courses = copy.deepcopy([x for x in item.preferred_courses if x in present_faculty_courses])


print("--------------------")

# Print Test of Loading Functions
unit = 0
print("Faculty List")
for item in faculty_list:
    print(item.professor_id, item.first_name, item.last_name, item.load)
    unit += item.load
    for item2 in item.preferred_courses:
        print(item2)
print("\n")
print(unit)

unit = 0
print("Offering List")
for item in offering_list:
    print(item.offering_id, item.section, item.course_id, item.course_code, item.units, item.max_students, item.course_type, item.room_id)
    unit += item.units
print ("\n")

print(unit)
print("General Course List")
for item in general_course_list:
    print(item.course_code, item.section, item.faculty_name, item.room, item.start_year, item.end_year, item.term, item.start_time, item.end_time, item.day1, item.day2)


for item in general_course_list:
    for item2 in timeslot_list:
        if item.day1 == item2.class_day and item.room == item2.room_code and item.start_time == item2.begin_time:
            item2.offering_id = item.course_code + " " + item.section + " " + "GE"
        if item.day2 == item2.class_day and item.room == item2.room_code and item.start_time == item2.begin_time:
            item2.offering_id = item.course_code + " " + item.section + " " + "GE"

print("Timeslot List")
for item in timeslot_list:
    print(item.timeslot_id, item.room_id, item.class_day, item.begin_time, item.end_time, item.room_type, item.room_code, item.room_capacity, item.offering_id)
print ("\n")

print("Section List")
for item in section_list:
    print(item.section_id, item.section_schedule)
print("\n")



# Assigns Faculty to Offerings and Offerings to Timeslots

#Change pop_size for population number
pop_size = 100
for x in range(pop_size):
    population.append(initialize(copy.deepcopy(faculty_list), copy.deepcopy(offering_list), copy.deepcopy(timeslot_list)))

print(len(population))


for x in population:
    x.fitness1 = fitness_function_1(x.faculty)
    x.fitness2 = fitness_function_2(x.faculty)
    print("Fitness Score 1: ", x.fitness1)
    print("Fitness Score 2: ", x.fitness2)
    print("-------------")


temp_fit = 50

timetable1 = Timetable
timetable2 = Timetable
timetable3 = Timetable

for x in population:
    if x.fitness1 < temp_fit:
        temp_fit = x.fitness1
        timetable1 = x
temp_fit = 50

for x in population:
    if x.fitness2 < temp_fit:
        temp_fit = x.fitness2
        timetable2 = x
temp_fit = 50


print("***Best of the Best - Fitness 1***")
print("Fitness Score 1: ", timetable1.fitness1)
print("Fitness Score 2: ", timetable1.fitness2)



print("***Best of the Best - Fitness 2***")
print("Fitness Score 1: ", timetable2.fitness1)
print("Fitness Score 2: ", timetable2.fitness2)


output_faculty_csv(timetable1)
output_timetable_csv(timetable1)
output_timeslots_csv(timetable1)

#-----------------------------------------------------------------------------------------------------------------------

# Selection and Population

#change generations for how many times it loops
generations = 100
for x in range(generations):
    numParentA = tournament_selection(population)
    print(numParentA)

    numParentB = numParentA

    while numParentB == numParentA:
        numParentB = tournament_selection(population)

    print(numParentB)

    if population[numParentA].fitness2 <= population[numParentB].fitness2:
        superParent = copy.deepcopy(population[numParentA])
        inferiorParent = copy.deepcopy((population[numParentB]))
    else:
        superParent = copy.deepcopy(population[numParentB])
        inferiorParent = copy.deepcopy((population[numParentA]))
    # Crossover


    emptyChild = Timetable(copy.deepcopy(faculty_list), copy.deepcopy(offering_list) , copy.deepcopy(timeslot_list))

    newChild = crossover_process(copy.deepcopy(superParent), copy.deepcopy(inferiorParent), copy.deepcopy(emptyChild))
    print("it is finished")


    newChild.fitness1 = fitness_function_1(newChild.faculty)
    newChild.fitness2 = fitness_function_2(newChild.faculty)

    population.sort(key=lambda x: x.fitness2)

    if newChild.fitness2 <= population[len(population)-1].fitness2:
        del population[len(population)-1]
        population.append(newChild)

#Output best timetable to csv
population.sort(key=lambda x: x.fitness2)
print(population[len(population)-1].fitness2)
print(population[0].fitness2)

#Average fitness for last generation
avg_total = 0.0
for item in population:
    avg_total += item.fitness2
avg_total = avg_total/pop_size


print("************************************************************************************************************************************")
print("                                                             Important Data                                                         ")
print("************************************************************************************************************************************")
print("Run Time: {0} seconds ".format(time.time() - startTime) )
print("No. of Generations: " + str(generations))
print("Population Size: " + str(pop_size))
print("Average Fitness for Latest Generation: " + str(avg_total))
print("Fittest Member: " + str(population[0].fitness2))
print("Least Fit Member: " + str(population[pop_size - 1].fitness2))
print("Total No. of Faculty Units: " + str(total_faculty_load))
print("Total No. of Offering Units: " + str(total_offering_units))
print("Total No. of Remaining Units: " + str(total_remaining_units))
print("Unassigned Offerings List: ")
print(unassigned_offering_list)

output_faculty_csv(population[0])
output_timetable_csv(population[0])
output_timeslots_csv(population[0])

