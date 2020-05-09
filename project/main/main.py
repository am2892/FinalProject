from flask import render_template, Blueprint, redirect, url_for, request, flash, session
from flask_login import login_required, current_user
import datetime
from ..cal.cal import random_cal
from ..models import Event
from ..app import db
import holidays
from datetime import date
import calendar

main_bp = Blueprint('main', __name__, template_folder='templates')

@main_bp.route("/")
def index():
    print("test here")
    return render_template("index.html")

@main_bp.route("/profile")
@login_required
def profile():
    return render_template("profile.html", name=current_user.name)

@main_bp.route("/calendar")
@login_required
def calendar():
    now = datetime.datetime.now()
    return redirect(url_for('cal.random_cal', year=now.year, month=now.month))

#@main_bp.route("/calendar")
#@login_required
#def calendar():
#    now = datetime.datetime.now()
#    us_holidays = holidays.US()
#    return random_cal(now.year, now.month,{
#        1: ["example"],
#        8: ["no."],
#        19: ["bye."]
#    })

@main_bp.route("/calendar", methods=['POST'])
def events_post():
    print(request.form)
    eventtitle = request.form.get('eventtitle')
    print (eventtitle)
    eventdesc = request.form.get('eventdesc')
    print (eventdesc)
    starttime = request.form.get('starttime')
    print (starttime)
    endtime = request.form.get('endtime')
    print (endtime)

    if endtime < starttime:
        flash('End date and time cannot occur before start date and time. Try again.')
        return redirect(url_for('main.calendar'))

    else:
        # TODO sqlalchemy.exc.StatementError: (builtins.TypeError) SQLite DateTime type only accepts Python datetime and date objects as input.
        # received format ValueError: time data '2020-05-08T00:00'
        # TODO check if correct format string: https://www.journaldev.com/23365/python-string-to-datetime-strptime
        starttime = datetime.datetime.strptime(starttime, '%Y-%m-%dT%H:%M')
        endtime = datetime.datetime.strptime(endtime, '%Y-%m-%dT%H:%M')
        new_event = Event(eventtitle=eventtitle, eventdesc=eventdesc, starttime=starttime, endtime=endtime)

        db.session.add(new_event)
        db.session.commit()

        flash('Event successfully added!')
        return redirect(url_for('main.calendar'))
