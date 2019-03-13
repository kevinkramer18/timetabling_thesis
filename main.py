# Import Classes
from professor import Professor
from course import Course
from offering import Offering
from timeslot import Timeslot


# Import Functions from Loading
from loading import load_course_list
from loading import load_faculty_list
from loading import load_offering_list
from loading import load_timeslot_list


# Import Functions from Initialization
from initialization import initialize


# List declarations
course_list = list(load_course_list())
faculty_list = list(load_faculty_list())
offering_list = list(load_offering_list())
timeslot_list = list(load_timeslot_list())



# Print Test of Loading Functions
print("Faculty List")
for item3 in faculty_list:
    print(item3.professor_id, item3.first_name, item3.last_name, item3.load)
    for item6 in item3.preferred_courses:
        print(item6)
print("\n")

print("Offering List")
for item4 in offering_list:
    print(item4.offering_id, item4.section, item4.course_id, item4.course_code, item4.units, item4.max_students, item4.course_type, item4.room_id, item4.flowchart_id)
print ("\n")

print("Timeslot List")
for item5 in timeslot_list:
    print(item5.timeslot_id, item5.room_id, item5.class_day, item5.begin_time, item5.end_time, item5.room_type, item5.room_code, item5.room_capacity)
print ("\n")


# Assigns Faculty to Offerings and Offerings to Timeslots
initialize(faculty_list, offering_list, timeslot_list)
