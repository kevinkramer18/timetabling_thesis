import random



def initialize(faculty_list, offering_list):

    for item in offering_list:
        boolean = False
        while not boolean:
            rand = random.randint(0, len(faculty_list)-1)
            if faculty_list[rand].load >= item.units:
                item.professor_id = faculty_list[rand].professor_id
                faculty_list[rand].load -= item.units
                faculty_list[rand].units += item.units
                boolean = True
            elif faculty_list[rand].load < item.units:
                boolean = False


            ''' 
            try:
                rand = random.randint(0, len(faculty_list)-1)
            if faculty_list[rand].load > item.units:
                item.professor_id = faculty_list[rand].professor_id
                faculty_list[rand].units += item.units
                faculty_list[rand].load -= item.units
                boolean = 1
            '''


    for object in offering_list:
        print(object.professor_id, object.course_code, object.section)
    for object2 in faculty_list:
        print(object2.professor_id, object2.first_name, object2.last_name, object2.load, object2.units)




