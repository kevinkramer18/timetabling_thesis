class Offering:
    professor_id = "1"
    room_id = "60"
    timeslot1_id = 0
    timeslot2_id = 0
    college_id = 0

    def __init__(self, offering_id, section, course_id, course_code, units, max_students, course_type, flowchart_id):
        self.offering_id = offering_id
        self.section = section
        self.course_id = course_id
        self.course_code = course_code
        self.units = units
        self.max_students = max_students
        self.course_type = course_type
        self.flowchart_id = flowchart_id






