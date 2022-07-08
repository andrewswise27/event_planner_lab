from datetime import date, datetime


class Event:
    def __init__(self, date, event_name, guests_num, room_loc, description, recurring):
        self.date = date
        date = datetime
        self.event_name = event_name
        self.guests_num = guests_num
        self.room_loc = room_loc
        self.description = description
        self.recurring = recurring

