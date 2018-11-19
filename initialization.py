import random



def initialize(faculty_list, offering_list):
    boolean = 0
    rand = 0
    for item in offering_list:
        while boolean != 1:
            rand = random.randint(0, len(faculty_list)-1)
            if faculty_list[rand].units < faculty_list[rand].load :
                item.professor_id = faculty_list[rand].professor_id
                faculty_list[rand].units += item.units
                ''''''
                if faculty_list[rand].units > faculty_list[rand].load :
                    faculty_list[rand].units -= item.units
                    item.professor_id = "1"
                    boolean = 0
                elif faculty_list[rand].units < faculty_list[rand].load or faculty_list[rand].units == faculty_list[rand].load:
                    boolean = 1
    for object in offering_list:
        print(object.professor_id, object.course_code, object.section)
    for object2 in faculty_list:
        print(object2.first_name, object2.last_name, object2.load, object2.units)




