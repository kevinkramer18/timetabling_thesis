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
# Import Functions from Initialization
from initialization import initialize
import copy

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

for x in range(100):
    population.append(initialize(copy.deepcopy(faculty_list), copy.deepcopy(offering_list), copy.deepcopy(timeslot_list)))

print(len(population))


for x in population:
    x.fitness1 = fitness_function_1(x.faculty)
    x.fitness2 = fitness_function_2(x.faculty)
    x.fitness3 = fitness_function_3(x.faculty)
    print("Fitness Score 1: ", x.fitness1)
    print("Fitness Score 2: ", x.fitness2)
    print("Fitness Score 3: ", x.fitness3)
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
for x in population:
    if x.fitness3 < temp_fit:
        temp_fit = x.fitness3
        timetable3 = x

print("***Best of the Best - Fitness 1***")
print("Fitness Score 1: ", timetable1.fitness1)
print("Fitness Score 2: ", timetable1.fitness2)
print("Fitness Score 3: ", timetable1.fitness3)


print("***Best of the Best - Fitness 2***")
print("Fitness Score 1: ", timetable2.fitness1)
print("Fitness Score 2: ", timetable2.fitness2)
print("Fitness Score 3: ", timetable2.fitness3)

print("***Best of the Best - Fitness 3***")
print("Fitness Score 1: ", timetable3.fitness1)
print("Fitness Score 2: ", timetable3.fitness2)
print("Fitness Score 3: ", timetable3.fitness3)