import copy
def fitness_function_1 (faculty_list):
    mViolations = 0
    aViolations = 0
    score = 0

    for item in faculty_list:
        mViolations += len(item.preferred_courses)

    for item in faculty_list:
        if len(item.preferred_courses) != 0:
            for x in item.preferred_courses:
                if x not in item.assigned_offerings:
                    aViolations += 1
    print("--------------------------")
    print(str(aViolations) + "/" + str(mViolations))
    print("--------------------------")
    score = aViolations/mViolations

    return score






def fitness_function_3 (faculty_list):
    aViolations = 0
    score = 0

    temp_list = []
    day_list = []
    time_list = []
    temp_sum = 0



    for item in faculty_list:
        if len(item.preferred_courses) != 0:
            for x in item.preferred_courses:
                if x not in item.assigned_offerings:
                    aViolations += 1

    for item in faculty_list:
        if len(item.schedule) >= 2:
            for item2 in item.schedule:
                temp_list = copy.deepcopy(item2.split('-'))
                day_list.append(str(temp_list[0]))
                time_list.append(int(temp_list[1]))
          #  for x in range(len(day_list)):
          #      day






    score = aViolations

    return score







#For Initialisation

def section_checking(timeslot, section, section_list):
    boolean = True
    for item in section_list:
        if section == item.section_id:
            for x in item.section_schedule:
                if timeslot == x:
                    boolean = False

    return boolean


def faculty_checking(faculty, nTimeslot):
    temp_list = []
    print(nTimeslot)
    temp_list = copy.deepcopy(nTimeslot.split('-'))
    print(temp_list)
    print("-------------")
    temp_day = str(temp_list[0])
    temp_slot = int(temp_list[1])
    temp_slot2 = 0

    boolean = True
    time_list = []



    if len(faculty.schedule) >= 2:
        for item in faculty.schedule:
            temp_list = copy.deepcopy(item.split('-'))
            print(temp_list)
            if temp_day == temp_list[0]:
                time_list.append(int(temp_list[1]))




        #Finds first consecutive class
        for item in time_list:
            print('duck')
            if temp_slot > item and (temp_slot - 185) == item and temp_slot2 == 0:
                temp_slot2 = item
                print("retardless")
                break
            elif temp_slot < item and (temp_slot + 185) == item and temp_slot2 == 0:
                temp_slot2 = item
                print("retardmore")
                break

        #Finds second consecutive class
        for item in time_list:
            print("fishsticks")
            if temp_slot2 != item and item < temp_slot and (temp_slot - 185) == item:
                boolean = False
                break
            elif temp_slot2 != item and item > temp_slot and (temp_slot + 185) == item:
                boolean = False
                break
            elif temp_slot2 != item and item < temp_slot2 and (temp_slot2 - 185) == item:
                boolean = False
                break
            elif temp_slot2 != item and item > temp_slot2 and (temp_slot2 +185) == item:
                boolean = False
                break



    return boolean

