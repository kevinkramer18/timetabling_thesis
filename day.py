class Day:
    offering_id = ""

    def __init__(self, days_id, room_id, class_day, begin_time, end_time, room_type, room_code, room_capacity):
        self.days_id = days_id
        self.room_id = room_id
        self.class_day = class_day
        self.begin_time = begin_time
        self.end_time = end_time
        self.room_type = room_type
        self.room_code = room_code
        self.room_capacity = room_capacity
