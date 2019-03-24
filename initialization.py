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
            rand = random.randint(0, len(timeslot_list) - 1)
            if item.course_type == timeslot_list[rand].room_type and item.max_students == timeslot_list[rand].room_capacity and timeslot_list[rand].offering_id == "":
                if item.units == 1:
                        timeslot_list[rand].offering_id = item.offering_id
                        item.timeslot1_id = timeslot_list[rand].timeslot_id
                        item.room_id = timeslot_list[rand].room_code



                elif item.units == 3:
                    if  timeslot_list[rand].class_day == 'M' and timeslot_list[rand+1].offering_id == "":
                        timeslot_list[rand].offering_id = item.offering_id
                        timeslot_list[rand+1].offering_id = item.offering_id
                        item.timeslot1_id = timeslot_list[rand].timeslot_id
                        item.timeslot2_id = timeslot_list[rand+1].timeslot_id
                        item.room_id = timeslot_list[rand].room_code

                    elif timeslot_list[rand].class_day == 'W' and timeslot_list[rand-1].offering_id == "":
                        timeslot_list[rand].offering_id = item.offering_id
                        timeslot_list[rand-1].offering_id = item.offering_id
                        item.timeslot1_id = timeslot_list[rand-1].timeslot_id
                        item.timeslot2_id = timeslot_list[rand].timeslot_id
                        item.room_id = timeslot_list[rand].room_code

                    elif timeslot_list[rand].class_day == 'T' and timeslot_list[rand+1].offering_id == "":
                        timeslot_list[rand].offering_id = item.offering_id
                        timeslot_list[rand+1].offering_id = item.offering_id
                        item.timeslot1_id = timeslot_list[rand].timeslot_id
                        item.timeslot2_id = timeslot_list[rand+1].timeslot_id
                        item.room_id = timeslot_list[rand].room_code

                    elif timeslot_list[rand].class_day == 'H'and timeslot_list[rand-1].offering_id == "":
                        timeslot_list[rand].offering_id = item.offering_id
                        timeslot_list[rand-1].offering_id = item.offering_id
                        item.timeslot1_id = timeslot_list[rand - 1].timeslot_id
                        item.timeslot2_id = timeslot_list[rand].timeslot_id
                        item.room_id = timeslot_list[rand].room_code

                    elif timeslot_list[rand].class_day == 'F' and timeslot_list[rand+1].offering_id == "":
                        timeslot_list[rand].offering_id = item.offering_id
                        timeslot_list[rand+1].offering_id = item.offering_id
                        item.timeslot1_id = timeslot_list[rand].timeslot_id
                        item.timeslot2_id = timeslot_list[rand+1].timeslot_id
                        item.room_id = timeslot_list[rand].room_code

                print("test")
                boolean = True
            else:
                boolean = False


# Checks for offerings that weren't assigned properly


# Checks for Faculty Schedule
    for test in offering_list:
        print(test.course_id, test.course_code, test.timeslot1_id, test.timeslot2_id, test.section, test.professor_id, test.room_id)
