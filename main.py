# Import Classes
from professor import Professor
from room import Room
from course import Course
from offering import Offering
from day import Day

# Loading lists of rooms, courses, & faculty
from loading import load_course_list
from loading import load_room_list
from loading import load_faculty_list
from loading import load_offering_list

course_list = list(load_course_list())
room_list = list(load_room_list())
faculty_list = list(load_faculty_list())
offering_list = list(load_offering_list())
day_list = list()

for item in course_list:
    print(item.course_id, item.college_id, item.dept_id, item.course_code, item.units, item.course_type)
print("\n")
for item2 in room_list:
    print(item2.room_id, item2.room_code, item2.room_type, item2.room_capacity)
print("\n")
for item3 in faculty_list:
    print(item3.user_id, item3.first_name, item3.last_name, item3.load)
print("\n")
for item4 in offering_list:
    print(item4.offering_id, item4.course_id, item4.section, item4.room_id)

