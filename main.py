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
from evaluation import fitness_function_3
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


# Removes offerings that are in excess of the faculty' total load limit and transfers them to a new list
unassigned_offering_list = []
total_offering_units  = 0.0


total_faculty_load = 0.0

for item in faculty_list:
    total_faculty_load += item.load

for i in range(0, len(offering_list)-1):
    if (total_offering_units + offering_list[i].units) <= total_faculty_load:
        total_offering_units += offering_list[i].units
    elif (total_offering_units + offering_list[i].units) > total_faculty_load:
        unassigned_offering_list.append(offering_list[i].course_code)
        total_offering_units -= offering_list[i].units
        print("Too many offerings")
        del offering_list[i]

print("Total number of units:" + str(total_offering_units))


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

for x in range(10):
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

# Selection

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

output_faculty_csv(newChild)
output_timetable_csv(newChild)
output_timeslots_csv(newChild)

