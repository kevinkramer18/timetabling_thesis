import random


def initialize(faculty_list, offering_list, timeslot_list):
    sections = []
# Assign offerings to faculty
    for item in offering_list:
        boolean = False
        while not boolean:
            print("assigning offerings to faculty")
            rand = random.randint(0, len(faculty_list)-1)
            if faculty_list[rand].load >= item.units:
                item.professor_id = faculty_list[rand].professor_id
                faculty_list[rand].load -= item.units
                faculty_list[rand].units += item.units
                faculty_list[rand].assigned_offerings.append(item.offering_id)
                boolean = True
            elif faculty_list[rand].load < item.units:
                boolean = False

# Display Offerings with Professors Assigned
    for object in offering_list:
        print(object.professor_id, object.course_code, object.section)
    print("\n")
# Display Faculty with Offerings assigned
    for object in faculty_list:
        print(object.professor_id, object.first_name, object.last_name, object.load, object.units)
    print("\n")


# Assign day timeslots to faculty's offerings

    for item in offering_list:
        boolean = False
        while not boolean:
            rand = random.randint(0, len(timeslot_list) - 2)
            for item2 in faculty_list:
                #this is the line i changed
                if item.offering_id in item2.assigned_offerings and timeslot_list[rand].class_day + str(timeslot_list[rand].begin_time) not in item2.schedule:
                    if item.course_type == timeslot_list[rand].room_type and item.max_students == timeslot_list[rand].room_capacity and timeslot_list[rand].offering_id == "":
                        if item.units == 1:
                            timeslot_list[rand].offering_id = item.offering_id
                            item.timeslot1_id = timeslot_list[rand].timeslot_id
                            item.room_id = timeslot_list[rand].room_code

                            item2.schedule.append(timeslot_list[rand].class_day + str(timeslot_list[rand].begin_time))

                        elif item.units == 3:
                            if timeslot_list[rand].class_day == 'M' and timeslot_list[rand + 1].offering_id == "":
                                timeslot_list[rand].offering_id = item.offering_id
                                timeslot_list[rand + 1].offering_id = item.offering_id
                                item.timeslot1_id = timeslot_list[rand].timeslot_id
                                item.timeslot2_id = timeslot_list[rand + 1].timeslot_id
                                item.room_id = timeslot_list[rand].room_code

                                item2.schedule.append(timeslot_list[rand].class_day + str(timeslot_list[rand].begin_time))
                                item2.schedule.append(timeslot_list[rand+1].class_day + str(timeslot_list[rand+1].begin_time))


                            elif timeslot_list[rand].class_day == 'W' and timeslot_list[rand - 1].offering_id == "":
                                timeslot_list[rand].offering_id = item.offering_id
                                timeslot_list[rand - 1].offering_id = item.offering_id
                                item.timeslot1_id = timeslot_list[rand - 1].timeslot_id
                                item.timeslot2_id = timeslot_list[rand].timeslot_id
                                item.room_id = timeslot_list[rand].room_code

                                item2.schedule.append( timeslot_list[rand].class_day + str(timeslot_list[rand].begin_time))
                                item2.schedule.append(timeslot_list[rand -1].class_day + str(timeslot_list[rand - 1].begin_time))

                            elif timeslot_list[rand].class_day == 'T' and timeslot_list[rand + 1].offering_id == "":
                                timeslot_list[rand].offering_id = item.offering_id
                                timeslot_list[rand + 1].offering_id = item.offering_id
                                item.timeslot1_id = timeslot_list[rand].timeslot_id
                                item.timeslot2_id = timeslot_list[rand + 1].timeslot_id
                                item.room_id = timeslot_list[rand].room_code

                                item2.schedule.append(timeslot_list[rand].class_day + str(timeslot_list[rand].begin_time))
                                item2.schedule.append(timeslot_list[rand + 1].class_day + str(timeslot_list[rand + 1].begin_time))

                            elif timeslot_list[rand].class_day == 'H' and timeslot_list[rand - 1].offering_id == "":
                                timeslot_list[rand].offering_id = item.offering_id
                                timeslot_list[rand - 1].offering_id = item.offering_id
                                item.timeslot1_id = timeslot_list[rand - 1].timeslot_id
                                item.timeslot2_id = timeslot_list[rand].timeslot_id
                                item.room_id = timeslot_list[rand].room_code

                                item2.schedule.append( timeslot_list[rand].class_day + str(timeslot_list[rand].begin_time))
                                item2.schedule.append( timeslot_list[rand - 1].class_day + str(timeslot_list[rand - 1].begin_time))

                            elif timeslot_list[rand].class_day == 'F' and timeslot_list[rand + 1].offering_id == "" and timeslot_list[rand].begin_time != 1245:
                                timeslot_list[rand].offering_id = item.offering_id
                                timeslot_list[rand + 1].offering_id = item.offering_id
                                item.timeslot1_id = timeslot_list[rand].timeslot_id
                                item.timeslot2_id = timeslot_list[rand + 1].timeslot_id
                                item.room_id = timeslot_list[rand].room_code

                                item2.schedule.append(timeslot_list[rand].class_day + str(timeslot_list[rand].begin_time))
                                item2.schedule.append(timeslot_list[rand + 1].class_day + str(timeslot_list[rand + 1].begin_time))

                        print("test")
                        boolean = True
                    else:
                        boolean = False

    for item in offering_list:
        if item.timeslot1_id == 0:
            print("fuck")
    for item in faculty_list:
        print(item.first_name, item.last_name)
        for x in item.assigned_offerings:
            print(x)
        for y in item.schedule:
            print(y)
    # Checks for Faculty Schedule
    for test in offering_list:
        print(test.offering_id, test.course_code, test.timeslot1_id, test.timeslot2_id, test.section, test.professor_id, test.room_id)
    ''' 
        for item in faculty_list:
            for x in item.assigned_offerings:
                rand = random.randint(0, len(timeslot_list) - 1)
                for item2 in offering_list:
                    if x == item2.offering_id:
    '''


    '''
    
# Checks for offerings that weren't assigned properly
    for item in offering_list:
        if item.timeslot1_id == 0:
            print("fuck")
    print("-------------------------------")
    for item in offering_list:
        if item.timeslot1_id == 0:
            rand = random.randint(0, len(timeslot_list) - 1)
            if item.course_type == timeslot_list[rand].room_type and item.max_students == timeslot_list[rand].room_capacity and timeslot_list[rand].offering_id == "":
                if timeslot_list[rand].class_day == 'M' and timeslot_list[rand + 1].offering_id == "":
                    timeslot_list[rand].offering_id = item.offering_id
                    timeslot_list[rand + 1].offering_id = item.offering_id
                    item.timeslot1_id = timeslot_list[rand].timeslot_id
                    item.timeslot2_id = timeslot_list[rand + 1].timeslot_id
                    item.room_id = timeslot_list[rand].room_code

                elif timeslot_list[rand].class_day == 'W' and timeslot_list[rand - 1].offering_id == "":
                    timeslot_list[rand].offering_id = item.offering_id
                    timeslot_list[rand - 1].offering_id = item.offering_id
                    item.timeslot1_id = timeslot_list[rand - 1].timeslot_id
                    item.timeslot2_id = timeslot_list[rand].timeslot_id
                    item.room_id = timeslot_list[rand].room_code

                elif timeslot_list[rand].class_day == 'T' and timeslot_list[rand + 1].offering_id == "":
                    timeslot_list[rand].offering_id = item.offering_id
                    timeslot_list[rand + 1].offering_id = item.offering_id
                    item.timeslot1_id = timeslot_list[rand].timeslot_id
                    item.timeslot2_id = timeslot_list[rand + 1].timeslot_id
                    item.room_id = timeslot_list[rand].room_code

                elif timeslot_list[rand].class_day == 'H' and timeslot_list[rand - 1].offering_id == "":
                    timeslot_list[rand].offering_id = item.offering_id
                    timeslot_list[rand - 1].offering_id = item.offering_id
                    item.timeslot1_id = timeslot_list[rand - 1].timeslot_id
                    item.timeslot2_id = timeslot_list[rand].timeslot_id
                    item.room_id = timeslot_list[rand].room_code

                elif timeslot_list[rand].class_day == 'F' and timeslot_list[rand + 1].offering_id == "":
                    timeslot_list[rand].offering_id = item.offering_id
                    timeslot_list[rand + 1].offering_id = item.offering_id
                    item.timeslot1_id = timeslot_list[rand].timeslot_id
                    item.timeslot2_id = timeslot_list[rand + 1].timeslot_id
                    item.room_id = timeslot_list[rand].room_code

    for item in offering_list:
        if item.timeslot1_id == 0:
            print("fuck")
    '''
    #for item2 in faculty_list:
    #   if item.offering_id in item2.assigned_offerings and timeslot_list[rand].class_day + str(timeslot_list[rand].begin_time) not in item2.schedule: