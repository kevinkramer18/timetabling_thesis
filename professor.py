class Professor:

    def __init__(self, user_id, first_name, last_name,  load):
        self.professor_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.load = load
        self.preferred_courses = []
        self.assigned_offerings = []
        self.units = 0
