from models.event import Event


event1 = Event((7, 7, 2022), 'Mental Health Webinar', 8, 'Castle Street', 'Mens Mental Health Webinar', False)
event2 = Event((7, 10, 2022), 'Premier League Watch Party', 75000, 'Old Trafford', "Not a watch party, we're at the game", True)
event3 = Event((6, 1, 2023), 'E59 Reunion', 22, 'The Chanter', 'Pints', False)

events = [event1, event2, event3]

def add_new_event(event):
    events.append(event)