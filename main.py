# Import Classes
from professor import Professor
from course import Course
from offering import Offering
from timeslot import Timeslot
from generalcourse import GeneralCourse

# Import Functions from Loading
from loading import load_course_list
from loading import load_faculty_list
from loading import load_offering_list
from loading import load_timeslot_list
from loading import load_general_course_list

# Import Functions from Initialization
from initialization import initialize


# List declarations
course_list = list(load_course_list())
faculty_list = list(load_faculty_list())
offering_list = list(load_offering_list())
timeslot_list = list(load_timeslot_list())
general_course_list = list(load_general_course_list())


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


print("General Course List")
for item6 in general_course_list:
    print(item6.course_code, item6.section, item6.faculty_name, item6.room, item6.start_year, item6.end_year, item6.term, item6.start_time, item6.end_time, item6.day1, item6.day2)


for item in general_course_list:
    for item2 in timeslot_list:
        if item.day1 == item2.class_day and item.room == item2.room_code and item.start_time == item2.begin_time:
            item2.offering_id = item.course_code + " " + item.section + " " + "GE"
        if item.day2 == item2.class_day and item.room == item2.room_code and item.start_time == item2.begin_time:
            item2.offering_id = item.course_code + " " + item.section + " " + "GE"

print("Timeslot List")
for item5 in timeslot_list:
    print(item5.timeslot_id, item5.room_id, item5.class_day, item5.begin_time, item5.end_time, item5.room_type, item5.room_code, item5.room_capacity, item5.offering_id)
print ("\n")

# Assigns Faculty to Offerings and Offerings to Timeslots
initialize(faculty_list, offering_list, timeslot_list)
