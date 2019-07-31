import copy

def fitness_function_1 (faculty_list):
    mViolations = 0
    aViolations = 0
    score = 0
    mw_time_list = []
    th_time_list = []
    f_time_list = []

    # Course Preference Violations
    for item in faculty_list:
        mViolations += len(item.preferred_courses)

    for item in faculty_list:
        if len(item.preferred_courses) != 0:
            for x in item.preferred_courses:
                if x not in item.assigned_courses:
                    aViolations += 1

    # Time Preferences Violations (Max long breaks between classes)
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

    # Underload Violations
    for x in faculty_list:
        if (x.units + x.load) == 12.0:
            mViolations +=1
    for x in faculty_list:
        if (x.units + x.load) == 12.0 and x.units != 12.0:
            aViolations +=1


    # Spread of Classes Violations

    for x in faculty_list:
        if (x.units + x.load) == 6:
            mViolations += 1
        elif (x.units + x.load) > 6:
            mViolations += 2

    for x in faculty_list:
        mCount = 0
        tCount = 0
        fCount = 0
        for y in x.schedule:
            temp_list = copy.deepcopy(y.split('-'))
            if temp_list[0] == 'M':
                mCount += 1
            elif temp_list[0] == 'T':
                tCount += 1
            elif temp_list[0] == 'F':
                fCount += 1
        if len(x.schedule) == 4:
            if mCount >= 1 and tCount >=1 or mCount >=1 and fCount >=1 or tCount >=1 and fCount >=1:
                aViolations +=1
        elif len(x.schedule) > 4:
            if mCount >= 1 and tCount >= 1 and fCount >= 1:
                aViolations +=2

    # Max Preparations
    for x in faculty_list:
        if len(x.assigned_courses) >= 4:
            mViolations += 1

    for x in faculty_list:
        if len(x.assigned_courses) >= 4:
            list_set = set(x.assigned_courses)
            # convert the set to the list
            unique_list = (list(list_set))
            if len(unique_list) >= 4:
                aViolations += 1

    print("Actual Violation: ", aViolations, "Maximum Violations: ", mViolations)

    score = aViolations/mViolations
    return score



def fitness_function_2(faculty_list):

    aViolations = 0

    # Change these Percentages for the Fitness Function 2 Tests
    pfc_percentage = 0.35
    tfc_percentage =  0.35
    under_percentage = 0.1
    spread_percentage = 0.1
    prep_percentage = 0.1

    pfc_a_count = 0
    spread_count = 0
    under_count = 0
    prep_count = 0

    mw_time_list = []
    th_time_list = []
    f_time_list = []

    # Course Preference Violations
    for item in faculty_list:
        if len(item.preferred_courses) != 0:
            for x in item.preferred_courses:
                if x not in item.assigned_courses:
                    pfc_a_count += 1


    # Time Preference Violations (Max long breaks in between classes)

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

    # Underload Violations
    for x in faculty_list:
        if (x.units + x.load) == 12.0 and x.units != 12.0:
            under_count += 1

    # Spread of Classes Violations
    for x in faculty_list:
        mCount = 0
        tCount = 0
        fCount = 0
        for y in x.schedule:
            temp_list = copy.deepcopy(y.split('-'))
            if temp_list[0] == 'M':
                mCount += 1
            elif temp_list[0] == 'T':
                tCount += 1
            elif temp_list[0] == 'F':
                fCount += 1
        if len(x.schedule) == 4:
            if mCount >= 1 and tCount >= 1 or mCount >= 1 and fCount >= 1 or tCount >= 1 and fCount >= 1:
                spread_count += 1
        elif len(x.schedule) > 4:
            if mCount >= 1 and tCount >= 1 and fCount >= 1:
                spread_count += 2


    # Max Preparations
    for x in faculty_list:
        if len(x.assigned_courses) >= 4:
            list_set = set(x.assigned_courses)
            # convert the set to the list
            unique_list = (list(list_set))
            if len(unique_list) >= 4:
                prep_count += 1

    print(aViolations,'*', tfc_percentage, '   ', pfc_a_count, '*', pfc_percentage, '  ', under_count, '*', under_percentage, "  ",spread_count, '*', spread_percentage, "  ",prep_count, '*', prep_percentage)
    score = (aViolations * tfc_percentage)+(pfc_a_count * pfc_percentage)+ (under_count * under_percentage)+ (spread_count *spread_percentage) + (prep_count * prep_percentage)

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

