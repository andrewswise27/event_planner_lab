from app import app
from flask import render_template, request, redirect
from models.event_list import events, add_new_event
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', events=events)

@app.route('/events', methods=['POST'])
def add_event():
    event_name = request.form['event-name']
    event_date = request.form['event-date']
    num_guests = request.form['num-guests']
    event_loc = request.form['event-location']
    event_desc = request.form['description']
    event_keys = request.form.keys()
    if 'input-checkbox' in event_keys:
        recurring_event = request.form['input-checkbox']
    else:
        recurring_event = False
    new_event = Event(event_date, event_name, num_guests, event_loc, event_desc, recurring_event)
    add_new_event(new_event)
    return redirect('/events')
