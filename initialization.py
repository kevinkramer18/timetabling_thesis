import random

rand = 0
count = 0
boolean = 0
def initialize(faculty_list, offering_list, course_list):
    for item in offering_list:
        while boolean != 1:
            rand = random.randint(0, len(faculty_list)-1)
            if faculty_list[rand].units < faculty_list[rand].load :
                item.professor_id = faculty_list[rand].professor_id
                faculty_list[rand].units += item.units
 

