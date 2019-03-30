
def fitness_function_1 (faculty_list):
    mViolations = 0
    aViolations = 0
    score = 0

    for item in faculty_list:
        mViolations += len(item.preferred_courses)

    for item in faculty_list:
        if len(item.preferred_courses) != 0:
            for x in item.preferred_courses:
                if x not in item.assigned_courses:
                    aViolations += 1
    score = aViolations/mViolations

    return score






def fitness_function_3 (faculty_list):
    aViolations = 0
    score = 0

    for item in faculty_list:
        if len(item.preferred_courses) != 0:
            for x in item.preferred_courses:
                if x not in item.assigned_courses:
                    aViolations += 1
    score = aViolations

    return score



def section_checking(timeslot, section, section_list):
    boolean = True
    for item in section_list:
        if section == item.section_id:
            for x in item.section_schedule:
                if timeslot == x:
                    boolean = False

    return boolean
