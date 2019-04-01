import random
import copy
from evaluation import section_checking
from evaluation import faculty_checking
from timetable import Timetable

def initialize(faculty_list, offering_list, timeslot_list):

# Transfer to local variables
    ifaculty_list = copy.deepcopy(faculty_list)
    ioffering_list = copy.deepcopy(offering_list)
    itimeslot_list = copy.deepcopy(timeslot_list)
    #isection_list = copy.deepcopy(section_list)
# Assign offerings to faculty

    for item in ioffering_list:
        boolean = False

        while not boolean:
            print("assigning offerings to faculty")
            rand = random.randint(0, len(ifaculty_list)-1)
            if ifaculty_list[rand].load >= item.units:
                item.professor_id = ifaculty_list[rand].professor_id
                ifaculty_list[rand].load -= item.units
                ifaculty_list[rand].units += item.units
                ifaculty_list[rand].assigned_offerings.append(item.offering_id)
                boolean = True
            elif ifaculty_list[rand].load < item.units:
                boolean = False

# Display Offerings with Professors Assigned
    for object in ioffering_list:
        print(object.professor_id, object.course_code, object.section)
    print("\n")
# Display Faculty with Offerings assigned
    for object in ifaculty_list:
        print(object.professor_id, object.first_name, object.last_name, object.load, object.units)
    print("\n")


# Assign day timeslots to faculty's offerings

    for item in ioffering_list:
        boolean = False
        while not boolean:
            rand = random.randint(0, len(timeslot_list) - 2)
            for item2 in ifaculty_list:
                #Checks if offering conflicts with professor's schedule and section schedule
                if item.offering_id in item2.assigned_offerings and itimeslot_list[rand].class_day + '-' + str(itimeslot_list[rand].begin_time) not in item2.schedule and faculty_checking(item2, itimeslot_list[rand].class_day + '-' + str(itimeslot_list[rand].begin_time)):
                    #Checks if room matches offering's requirements and that the timeslot isn't already taken
                    if item.course_type == itimeslot_list[rand].room_type and item.max_students == itimeslot_list[rand].room_capacity and itimeslot_list[rand].offering_id == "":
                        if item.units == 1:
                            itimeslot_list[rand].offering_id = item.offering_id
                            item.timeslot1_id = itimeslot_list[rand].timeslot_id
                            item.room_id = itimeslot_list[rand].room_code

                            #Updates Faculty schedule
                            item2.schedule.append(itimeslot_list[rand].class_day + '-' + str(itimeslot_list[rand].begin_time))



                        elif item.units == 3:
                            if itimeslot_list[rand].class_day == 'M' and itimeslot_list[rand + 1].offering_id == "":
                                itimeslot_list[rand].offering_id = item.offering_id
                                itimeslot_list[rand + 1].offering_id = item.offering_id
                                item.timeslot1_id = itimeslot_list[rand].timeslot_id
                                item.timeslot2_id = itimeslot_list[rand + 1].timeslot_id
                                item.room_id = itimeslot_list[rand].room_code

                                # Updates Faculty Schedule
                                item2.schedule.append(itimeslot_list[rand].class_day + '-' + str(itimeslot_list[rand].begin_time))
                                item2.schedule.append(itimeslot_list[rand+1].class_day + '-' + str(itimeslot_list[rand+1].begin_time))





                            elif itimeslot_list[rand].class_day == 'W' and itimeslot_list[rand - 1].offering_id == "":
                                itimeslot_list[rand].offering_id = item.offering_id
                                itimeslot_list[rand - 1].offering_id = item.offering_id
                                item.timeslot1_id = itimeslot_list[rand - 1].timeslot_id
                                item.timeslot2_id = itimeslot_list[rand].timeslot_id
                                item.room_id = itimeslot_list[rand].room_code

                                #Updates Faculty Schedule

                                item2.schedule.append( itimeslot_list[rand].class_day + '-' + str(itimeslot_list[rand].begin_time))
                                item2.schedule.append(itimeslot_list[rand -1].class_day + '-' + str(itimeslot_list[rand - 1].begin_time))





                            elif itimeslot_list[rand].class_day == 'T' and itimeslot_list[rand + 1].offering_id == "":
                                itimeslot_list[rand].offering_id = item.offering_id
                                itimeslot_list[rand + 1].offering_id = item.offering_id
                                item.timeslot1_id = itimeslot_list[rand].timeslot_id
                                item.timeslot2_id = itimeslot_list[rand + 1].timeslot_id
                                item.room_id = itimeslot_list[rand].room_code

                                #Updates Faculty Schedule
                                item2.schedule.append(itimeslot_list[rand].class_day + '-' + str(itimeslot_list[rand].begin_time))
                                item2.schedule.append(itimeslot_list[rand + 1].class_day + '-' + str(itimeslot_list[rand + 1].begin_time))


                            elif itimeslot_list[rand].class_day == 'H' and itimeslot_list[rand - 1].offering_id == "":
                                itimeslot_list[rand].offering_id = item.offering_id
                                itimeslot_list[rand - 1].offering_id = item.offering_id
                                item.timeslot1_id = itimeslot_list[rand - 1].timeslot_id
                                item.timeslot2_id = itimeslot_list[rand].timeslot_id
                                item.room_id = itimeslot_list[rand].room_code

                                # Updates Faculty Schedule

                                item2.schedule.append( itimeslot_list[rand].class_day + '-' + str(itimeslot_list[rand].begin_time))
                                item2.schedule.append( itimeslot_list[rand - 1].class_day + '-' + str(itimeslot_list[rand - 1].begin_time))




                            elif itimeslot_list[rand].class_day == 'F' and itimeslot_list[rand + 1].offering_id == "" and itimeslot_list[rand].begin_time != 1245:
                                itimeslot_list[rand].offering_id = item.offering_id
                                itimeslot_list[rand + 1].offering_id = item.offering_id
                                item.timeslot1_id = itimeslot_list[rand].timeslot_id
                                item.timeslot2_id = itimeslot_list[rand + 1].timeslot_id
                                item.room_id = itimeslot_list[rand].room_code

                                item2.schedule.append(itimeslot_list[rand].class_day + '-' + str(itimeslot_list[rand].begin_time))
                                item2.schedule.append(itimeslot_list[rand + 1].class_day + '-' + str(itimeslot_list[rand + 1].begin_time))



                        print("test")
                        if item.timeslot1_id == 0:
                            boolean = False
                        else:
                            boolean = True
                    else:
                        boolean = False


    for item in ifaculty_list:
        print(item.first_name, item.last_name)
        for x in item.assigned_offerings:
            print(x)
        for y in item.schedule:
            print(y)


    for item in ioffering_list:
        if item.timeslot1_id == 0:
            print("unassigned offering")
    # Checks for Faculty Schedule
    for test in ioffering_list:
        print(test.offering_id, test.course_code, test.timeslot1_id, test.timeslot2_id, test.section, test.professor_id, test.room_id)

    timetable = Timetable(ifaculty_list, ioffering_list, itimeslot_list)
    return timetable





'''# Assign day timeslots to faculty's offerings

    for item in ioffering_list:
        boolean = False
        while not boolean:
            rand = random.randint(0, len(timeslot_list) - 2)
            for item2 in ifaculty_list:
                #Checks if offering conflicts with professor's schedule and section schedule
                if section_checking(itimeslot_list[rand].class_day + str(itimeslot_list[rand].begin_time), item.section, isection_list) and item.offering_id in item2.assigned_offerings and itimeslot_list[rand].class_day + str(itimeslot_list[rand].begin_time) not in item2.schedule:
                    #Checks if room matches offering's requirements and that the timeslot isn't already taken
                    if item.course_type == itimeslot_list[rand].room_type and item.max_students == itimeslot_list[rand].room_capacity and itimeslot_list[rand].offering_id == "":
                        if item.units == 1:
                            itimeslot_list[rand].offering_id = item.offering_id
                            item.timeslot1_id = itimeslot_list[rand].timeslot_id
                            item.room_id = itimeslot_list[rand].room_code

                            #Updates Faculty schedule
                            item2.schedule.append(itimeslot_list[rand].class_day + str(itimeslot_list[rand].begin_time))

                            #Updates Section schedule
                            for x in isection_list:
                                if item.section == x.section_id:
                                    x.section_schedule.append(itimeslot_list[rand].class_day + str(itimeslot_list[rand].begin_time))
                                   # x.section_schedule.append( itimeslot_list[rand].class_day + str(itimeslot_list[rand].end_time))

                        elif item.units == 3:
                            if itimeslot_list[rand].class_day == 'M' and itimeslot_list[rand + 1].offering_id == "":
                                itimeslot_list[rand].offering_id = item.offering_id
                                itimeslot_list[rand + 1].offering_id = item.offering_id
                                item.timeslot1_id = itimeslot_list[rand].timeslot_id
                                item.timeslot2_id = itimeslot_list[rand + 1].timeslot_id
                                item.room_id = itimeslot_list[rand].room_code

                                # Updates Faculty Schedule
                                item2.schedule.append(itimeslot_list[rand].class_day + str(itimeslot_list[rand].begin_time))
                                item2.schedule.append(itimeslot_list[rand+1].class_day + str(itimeslot_list[rand+1].begin_time))

                                # Updates Section schedule
                                for x in isection_list:
                                    if item.section == x.section_id:
                                        x.section_schedule.append(itimeslot_list[rand].class_day + str(itimeslot_list[rand].begin_time))
                                     #   x.section_schedule.append(itimeslot_list[rand].class_day + str(itimeslot_list[rand].end_time))
                                        x.section_schedule.append(itimeslot_list[rand+1].class_day + str(itimeslot_list[rand+1].begin_time))
                                       # x.section_schedule.append( itimeslot_list[rand+1].class_day + str(itimeslot_list[rand+1].end_time))



                            elif itimeslot_list[rand].class_day == 'W' and itimeslot_list[rand - 1].offering_id == "":
                                itimeslot_list[rand].offering_id = item.offering_id
                                itimeslot_list[rand - 1].offering_id = item.offering_id
                                item.timeslot1_id = itimeslot_list[rand - 1].timeslot_id
                                item.timeslot2_id = itimeslot_list[rand].timeslot_id
                                item.room_id = itimeslot_list[rand].room_code

                                #Updates Faculty Schedule

                                item2.schedule.append( itimeslot_list[rand].class_day + str(itimeslot_list[rand].begin_time))
                                item2.schedule.append(itimeslot_list[rand -1].class_day + str(itimeslot_list[rand - 1].begin_time))

                                #Updates Section Schedule
                                for x in isection_list:
                                    if item.section == x.section_id:
                                        x.section_schedule.append(itimeslot_list[rand].class_day + str(itimeslot_list[rand].begin_time))
                                      #  x.section_schedule.append( itimeslot_list[rand].class_day + str(itimeslot_list[rand].end_time))
                                        x.section_schedule.append(itimeslot_list[rand - 1].class_day + str(itimeslot_list[rand - 1].begin_time))
                                     #   x.section_schedule.append(itimeslot_list[rand - 1].class_day + str(itimeslot_list[rand - 1].end_time))



                            elif itimeslot_list[rand].class_day == 'T' and itimeslot_list[rand + 1].offering_id == "":
                                itimeslot_list[rand].offering_id = item.offering_id
                                itimeslot_list[rand + 1].offering_id = item.offering_id
                                item.timeslot1_id = itimeslot_list[rand].timeslot_id
                                item.timeslot2_id = itimeslot_list[rand + 1].timeslot_id
                                item.room_id = itimeslot_list[rand].room_code

                                #Updates Faculty Schedule
                                item2.schedule.append(itimeslot_list[rand].class_day + str(itimeslot_list[rand].begin_time))
                                item2.schedule.append(itimeslot_list[rand + 1].class_day + str(itimeslot_list[rand + 1].begin_time))

                                # Updates Section schedule
                                for x in isection_list:
                                    if item.section == x.section_id:
                                        x.section_schedule.append( itimeslot_list[rand].class_day + str(itimeslot_list[rand].begin_time))
                                      #  x.section_schedule.append( itimeslot_list[rand].class_day + str(itimeslot_list[rand].end_time))
                                        x.section_schedule.append(itimeslot_list[rand+1].class_day + str(itimeslot_list[rand + 1].begin_time))
                                     #   x.section_schedule.append(itimeslot_list[rand+1].class_day + str(itimeslot_list[rand + 1].end_time))

                            elif itimeslot_list[rand].class_day == 'H' and itimeslot_list[rand - 1].offering_id == "":
                                itimeslot_list[rand].offering_id = item.offering_id
                                itimeslot_list[rand - 1].offering_id = item.offering_id
                                item.timeslot1_id = itimeslot_list[rand - 1].timeslot_id
                                item.timeslot2_id = itimeslot_list[rand].timeslot_id
                                item.room_id = itimeslot_list[rand].room_code

                                # Updates Faculty Schedule

                                item2.schedule.append( itimeslot_list[rand].class_day + str(itimeslot_list[rand].begin_time))
                                item2.schedule.append( itimeslot_list[rand - 1].class_day + str(itimeslot_list[rand - 1].begin_time))

                                # Updates Section Schedule
                                for x in isection_list:
                                    if item.section == x.section_id:
                                        x.section_schedule.append( itimeslot_list[rand].class_day + str(itimeslot_list[rand].begin_time))
                                      #  x.section_schedule.append(itimeslot_list[rand].class_day + str(itimeslot_list[rand].end_time))
                                        x.section_schedule.append(itimeslot_list[rand - 1].class_day + str(itimeslot_list[rand - 1].begin_time))
                                      #  x.section_schedule.append(itimeslot_list[rand - 1].class_day + str(itimeslot_list[rand - 1].end_time))


                            elif itimeslot_list[rand].class_day == 'F' and itimeslot_list[rand + 1].offering_id == "" and itimeslot_list[rand].begin_time != 1245:
                                itimeslot_list[rand].offering_id = item.offering_id
                                itimeslot_list[rand + 1].offering_id = item.offering_id
                                item.timeslot1_id = itimeslot_list[rand].timeslot_id
                                item.timeslot2_id = itimeslot_list[rand + 1].timeslot_id
                                item.room_id = itimeslot_list[rand].room_code

                                item2.schedule.append(itimeslot_list[rand].class_day + str(itimeslot_list[rand].begin_time))
                                item2.schedule.append(itimeslot_list[rand + 1].class_day + str(itimeslot_list[rand + 1].begin_time))

                                # Updates Section Schedule
                                for x in isection_list:
                                    if item.section == x.section_id:
                                        x.section_schedule.append(itimeslot_list[rand].class_day + str(itimeslot_list[rand].begin_time))
                                       # x.section_schedule.append(itimeslot_list[rand].class_day + str(itimeslot_list[rand].end_time))
                                        x.section_schedule.append( itimeslot_list[rand + 1].class_day + str(itimeslot_list[rand + 1].begin_time))
                                       # x.section_schedule.append(itimeslot_list[rand + 1].class_day + str(itimeslot_list[rand + 1].end_time))

                        print("test")
                        if item.timeslot1_id == 0:
                            boolean = False
                        else:
                            boolean = True
                    else:
                        boolean = False


    for item in ifaculty_list:
        print(item.first_name, item.last_name)
        for x in item.assigned_offerings:
            print(x)
        for y in item.schedule:
            print(y)


    for item in isection_list:
        print (item.section_id, item.section_schedule)

    for item in ioffering_list:
        if item.timeslot1_id == 0:
            print("unassigned offering")
    # Checks for Faculty Schedule
    for test in ioffering_list:
        print(test.offering_id, test.course_code, test.timeslot1_id, test.timeslot2_id, test.section, test.professor_id, test.room_id)

    timetable = Timetable(ifaculty_list, ioffering_list, itimeslot_list, isection_list)
'''