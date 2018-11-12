from professor import Professor
from room import Room
from course import Course
from offering import Offering

# Loading lists of rooms, courses, f
from loading import load_course_list
from loading import load_room_list

course_list = list(load_course_list())
room_list = list(load_room_list())

for item in course_list:
    print(item.course_id, item.college_id, item.dept_id, item.course_code, item.units, item.course_type)

for item2 in room_list:
    print(item2.room_id, item2.room_code, item2.room_type, item2.room_capacity)

#load_course_list()