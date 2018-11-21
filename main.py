# Import Classes
from professor import Professor
from room import Room
from course import Course
from offering import Offering
from day import Day


# Import Functions from Loading
from loading import load_course_list
from loading import load_room_list
from loading import load_faculty_list
from loading import load_offering_list
from loading import load_day_list

# Import Functions from Initialization
from initialization import initialize


# List declarations
course_list = list(load_course_list())
room_list = list(load_room_list())
faculty_list = list(load_faculty_list())
offering_list = list(load_offering_list())
day_list = list(load_day_list())



# Print Test of Loading Functions
'''
for item in course_list:
    print(item.course_id, item.college_id, item.dept_id, item.course_code, item.units, item.course_type)
print("\n")
'''
for item2 in room_list:
    print(item2.room_id, item2.room_code, item2.room_type, item2.room_capacity)
print("\n")
for item3 in faculty_list:
    print(item3.professor_id, item3.first_name, item3.last_name, item3.load)
print("\n")
for item4 in offering_list:
    print(item4.offering_id, item4.section, item4.course_id, item4.course_code, item4.units, item4.max_students, item4.course_type, item4.room_id)
print ("\n")
for item5 in day_list:
    print(item5.days_id, item5.room_id, item5.class_day, item5.begin_time, item5.end_time, item5.room_type, item5.room_code, item5.room_capacity)


# print(offering_list..index("1496"))

'''
for object in offering_list:
   if object.course_id == 1496:
       print(object.section)
'''
initialize(faculty_list, offering_list, room_list, day_list)