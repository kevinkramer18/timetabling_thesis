import random



def initialize(faculty_list, offering_list, room_list, timeslot_list):
    sections = []
  # Assign offerings to faculty
    for item in offering_list:
        boolean = False
        while not boolean:
            rand = random.randint(0, len(faculty_list)-1)
            if faculty_list[rand].load >= item.units:
                item.professor_id = faculty_list[rand].professor_id
                faculty_list[rand].load -= item.units
                faculty_list[rand].units += item.units
                faculty_list[rand].assigned_offerings.append(item.offering_id)
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

# THIS WORKS ABOVE^^^

    ''' 
    for item2 in offering_list:
        boolean = False
        while not boolean:
            rand = random.randint(0, len(day_list) - 1)
            if item2.course_type == room_list[room_list.index(day_list[rand].room_id)].room_type and item2.max_students == room_list[day_list[rand].room_id]:
    '''

    # Assign day timeslots to faculty's offerings
    for item2 in offering_list:
        boolean = False
        while not boolean:
            rand = random.randint(0, len(timeslot_list) - 1)
            if item2.course_type == timeslot_list[rand].room_type and item2.max_students == timeslot_list[rand].room_capacity and timeslot_list[rand].offering_id == "":
                if item2.units == 1:
                    timeslot_list[rand].offering_id = item2.offering_id
                    item2.timeslot1_id = timeslot_list[rand].timeslot_id

                elif item2.units == 3:
                    if  timeslot_list[rand].class_day == 'M' and timeslot_list[rand+1].offering_id == "":
                        timeslot_list[rand].offering_id = item2.offering_id
                        timeslot_list[rand+1].offering_id = item2.offering_id
                        item2.timeslot1_id = timeslot_list[rand].timeslot_id
                        item2.timeslot2_id = timeslot_list[rand+1].timeslot_id

                    elif timeslot_list[rand].class_day == 'W' and timeslot_list[rand-1].offering_id == "":
                        timeslot_list[rand].offering_id = item2.offering_id
                        timeslot_list[rand-1].offering_id = item2.offering_id
                        item2.timeslot1_id = timeslot_list[rand-1].timeslot_id
                        item2.timeslot2_id = timeslot_list[rand].timeslot_id

                    elif timeslot_list[rand].class_day == 'T' and timeslot_list[rand+1].offering_id == "":
                        timeslot_list[rand].offering_id = item2.offering_id
                        timeslot_list[rand+1].offering_id = item2.offering_id
                        item2.timeslot1_id = timeslot_list[rand].timeslot_id
                        item2.timeslot2_id = timeslot_list[rand+1].timeslot_id

                    elif timeslot_list[rand].class_day == 'H'and timeslot_list[rand-1].offering_id == "":
                        timeslot_list[rand].offering_id = item2.offering_id
                        timeslot_list[rand-1].offering_id = item2.offering_id
                        item2.timeslot1_id = timeslot_list[rand - 1].timeslot_id
                        item2.timeslot2_id = timeslot_list[rand].timeslot_id

                    elif timeslot_list[rand].class_day == 'F' and timeslot_list[rand+1].offering_id == "":
                        timeslot_list[rand].offering_id = item2.offering_id
                        timeslot_list[rand+1].offering_id = item2.offering_id
                        item2.timeslot1_id = timeslot_list[rand].timeslot_id
                        item2.timeslot2_id = timeslot_list[rand+1].timeslot_id

                    '''
                    timeslot_list[rand].offering_id = item2.offering_id
                    item2.timeslot1_id = timeslot_list[rand].timeslot_id
                    item2.timeslot2_id = timeslot_list[rand].timeslot_id
                    '''
                print("test")
                boolean = True
            else:
                boolean = False
    for test in offering_list:
        print(test.course_id, test.course_code, test.timeslot1_id, test.timeslot2_id, test.section, test.professor_id)
