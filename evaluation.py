import copy

def fitness_function_1 (faculty_list):
    mViolations = 0
    aViolations = 0
    score = 0
    mw_time_list = []
    th_time_list = []
    f_time_list = []

    for item in faculty_list:
        mViolations += len(item.preferred_courses)

    for item in faculty_list:
        if len(item.preferred_courses) != 0:
            for x in item.preferred_courses:
                if x not in item.assigned_offerings:
                    aViolations += 1

    # Max long breaks between classes
    for item in faculty_list:
        if len(item.schedule) >= 2:
            for item2 in item.schedule:
                temp_list = copy.deepcopy(item2.split('-'))
                if temp_list[0] == 'M':
                    mw_time_list.append(int(temp_list[1]))
                elif temp_list[0] == 'T':
                    th_time_list.append(int(temp_list[1]))
                elif temp_list[0] == 'F':
                    f_time_list.append(int(temp_list[1]))

        if len(mw_time_list) == 2:
            mViolations += 1
        elif len(mw_time_list) >= 3:
            mViolations += 2
        elif len(th_time_list) == 2:
            mViolations += 1
        elif len(th_time_list) >= 3:
            mViolations += 2
        elif len(f_time_list) == 2:
            mViolations += 1
        elif len(f_time_list) >= 3:
            mViolations += 2

        if len(mw_time_list) >= 2:
            mw_time_list.sort()
            for y in range(len(mw_time_list)-1):
                if (mw_time_list[y] + 435) <  mw_time_list[y+1]:
                   # print(mw_time_list[y])
                   # print(mw_time_list[y+1])
                    aViolations += 1

        elif len(th_time_list) >= 2:
            th_time_list.sort()
            for y in range(len(th_time_list)-1):
                if (th_time_list[y] + 435) <  th_time_list[y+1]:
                   # print(th_time_list[y])
                   # print(th_time_list[y + 1])
                    aViolations += 1

        elif len(f_time_list) >= 2:
            f_time_list.sort()
            for y in range(len(f_time_list)-1):
                if (f_time_list[y] + 435) <  f_time_list[y+1]:
                   # print(f_time_list[y])
                   # print(f_time_list[y + 1])
                    aViolations += 1


    print(aViolations, mViolations)

    score = aViolations/mViolations
    return score



def fitness_function_2(faculty_list):
    mViolations = 0
    aViolations = 0

    pfc_percentage = 0.6
    lb_percentage =  0.4

    pfc_a_count = 0
    lb_a_count = 0

    score = 0

    mw_time_list = []
    th_time_list = []
    f_time_list = []

    for item in faculty_list:
        if len(item.preferred_courses) != 0:
            for x in item.preferred_courses:
                if x not in item.assigned_offerings:
                    pfc_a_count += 1


    # Breaks in between classes

    for item in faculty_list:
        if len(item.schedule) >= 2:
            for item2 in item.schedule:
                temp_list = copy.deepcopy(item2.split('-'))
                if temp_list[0] == 'M':
                    mw_time_list.append(int(temp_list[1]))
                elif temp_list[0] =='T':
                    th_time_list.append(int(temp_list[1]))
                elif temp_list[0] == 'F':
                    f_time_list.append(int(temp_list[1]))

        if len(mw_time_list) >= 2:
            mw_time_list.sort()
            for y in range(len(mw_time_list)-1):
                if (mw_time_list[y] + 435) <  mw_time_list[y+1]:
                    #print(mw_time_list[y])
                    #print(mw_time_list[y+1])
                    aViolations += 1

        elif len(th_time_list) >= 2:
            th_time_list.sort()
            for y in range(len(th_time_list)-1):
                if (th_time_list[y] + 435) <  th_time_list[y+1]:
                    #print(th_time_list[y])
                    #print(th_time_list[y + 1])
                    aViolations += 1

        elif len(f_time_list) >= 2:
            f_time_list.sort()
            for y in range(len(f_time_list)-1):
                if (f_time_list[y] + 435) <  f_time_list[y+1]:
                   # print(f_time_list[y])
                   # print(f_time_list[y + 1])
                    aViolations += 1

    print(aViolations,'*', lb_percentage, '   ', pfc_a_count, '*', pfc_percentage)
    score = (aViolations * lb_percentage)+(pfc_a_count * pfc_percentage)

    return score





def fitness_function_3 (faculty_list):
    aViolations = 0
    score = 0

    temp_list = []
    day_list = []

    mw_time_list = []
    th_time_list = []
    f_time_list = []

    temp = 0
    temp2 = 0

    for item in faculty_list:
        if len(item.preferred_courses) != 0:
            for x in item.preferred_courses:
                if x not in item.assigned_offerings:
                    aViolations += 1


    # Breaks in between classes

    for item in faculty_list:
        if len(item.schedule) >= 2:
            for item2 in item.schedule:
                temp_list = copy.deepcopy(item2.split('-'))
                if temp_list[0] == 'M':
                    mw_time_list.append(int(temp_list[1]))
                elif temp_list[0] =='T':
                    th_time_list.append(int(temp_list[1]))
                elif temp_list[0] == 'F':
                    f_time_list.append(int(temp_list[1]))

        if len(mw_time_list) >= 2:
            mw_time_list.sort()
            for y in range(len(mw_time_list)-1):
                if (mw_time_list[y] + 435) <  mw_time_list[y+1]:
                    #print(mw_time_list[y])
                    #print(mw_time_list[y+1])
                    aViolations += 1

        elif len(th_time_list) >= 2:
            th_time_list.sort()
            for y in range(len(th_time_list)-1):
                if (th_time_list[y] + 435) <  th_time_list[y+1]:
                    #print(th_time_list[y])
                    #print(th_time_list[y + 1])
                    aViolations += 1

        elif len(f_time_list) >= 2:
            f_time_list.sort()
            for y in range(len(f_time_list)-1):
                if (f_time_list[y] + 435) <  f_time_list[y+1]:
                   # print(f_time_list[y])
                   # print(f_time_list[y + 1])
                    aViolations += 1




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


        if len(time_list) > 1:
            # Finds first consecutive class
            for item in time_list:
                print('duck')
                if temp_slot > item and ((temp_slot - item) == 185 or (temp_slot - item) == 145) and temp_slot2 == 0:
                    temp_slot2 = item
                    print("temp2")
                    break
                elif temp_slot < item and ((item - temp_slot) == 185 or (item - temp_slot) == 145) and temp_slot2 == 0:
                    temp_slot2 = item
                    print("temp2")
                    break

            # Finds second consecutive class
            for item in time_list:
                print("fishsticks")
                if temp_slot2 != item and item < temp_slot and ((temp_slot - item) == 185 or (temp_slot - item) == 145):
                    print("it work1")
                    boolean = False
                    break
                elif temp_slot2 != item and item > temp_slot and ((item - temp_slot) == 185 or (item - temp_slot) == 145):
                    print("it work2")
                    boolean = False
                    break
                elif temp_slot2 != item and item < temp_slot2 and ((temp_slot2 - item) == 185 or (temp_slot2 - item) == 145):
                    print("it work3")
                    boolean = False
                    break
                elif temp_slot2 != item and item > temp_slot2 and ((item - temp_slot2) == 185 or (item - temp_slot2) == 145):
                    print("it work4")
                    boolean = False
                    break

    return boolean

