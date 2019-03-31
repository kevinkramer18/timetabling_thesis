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
timetable_list = []


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
timetable_list.append(initialize(copy.deepcopy(faculty_list), copy.deepcopy(offering_list), copy.deepcopy(timeslot_list), copy.deepcopy(section_list)))
timetable_list.append(initialize(copy.deepcopy(faculty_list), copy.deepcopy(offering_list), copy.deepcopy(timeslot_list), copy.deepcopy(section_list)))

print(len(timetable_list))
