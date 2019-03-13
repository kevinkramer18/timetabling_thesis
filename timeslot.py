class Timeslot:

    def __init__(self, timeslot_id, room_id, class_day, begin_time, end_time, room_type, room_code, room_capacity):
        self.timeslot_id = timeslot_id
        self.room_id = room_id
        self.class_day = class_day
        self.begin_time = begin_time
        self.end_time = end_time
        self.room_type = room_type
        self.room_code = room_code
        self.room_capacity = room_capacity
        self.offering_id = ""
