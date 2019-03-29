
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

