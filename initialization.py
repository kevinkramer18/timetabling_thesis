import random



def initialize(faculty_list, offering_list):

    temp_list = faculty_list.copy()
    for item in offering_list:
        boolean = False
        while not boolean:
            rand = random.randint(0, len(temp_list)-1)
            if temp_list[rand].load >= item.units:
                # Changing value of faculty_list
                for item2 in faculty_list:
                    if item2.professor_id == temp_list[rand].professor_id:
                        item.professor_id = item2.professor_id
                        item2.load -= item.units
                        item2.units += item.units
                '''
                item.professor_id = faculty_list[rand].professor_id
                faculty_list[rand].load -= item.units
                faculty_list[rand].units += item.units
                '''
                temp_list[rand].load -= item.units
                temp_list[rand].units += item.units
            elif temp_list[rand].load < item.units:
                del  temp_list[rand]
                if len(temp_list) == 0:
                    break
            else:
                boolean = True




    for object in offering_list:
        print(object.professor_id, object.course_code, object.section)
    for object2 in faculty_list:
        print(object2.professor_id, object2.first_name, object2.last_name, object2.load, object2.units)
    print (len(faculty_list))




