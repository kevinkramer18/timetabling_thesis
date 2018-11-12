class Professor:

    def __init__(self, faculty_id, last_name, first_name, load, preferred_courses, preferred_timeslots):
        self.faculty_id = faculty_id
        self.last_name = last_name
        self.first_name = first_name
        self.units = 0
        self.load = load
        self.preferred_courses = list(preferred_courses)

