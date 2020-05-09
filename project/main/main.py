from flask import render_template, Blueprint, redirect, url_for, request, flash
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

#@main_bp.route("/<int:year>/<int:month>")
#@main_bp.route('/<int:year>/<int:month>')
#@login_required
#def calendar():
#    now = datetime.datetime.now()
#    for date , name in holidays.US(years = now.year).items():
#        if now.month == date.month:
#            return random_cal(date.year,date.month,{date.day:[name]})
#    return random_cal(now.year, now.month)

@main_bp.route("/calendar")
@login_required
def calendar():
    now = datetime.datetime.now()
    for date , name in holidays.US(years = now.year).items():
        if now.month == date.month:
            return random_cal(date.year,date.month,{date.day:[name]})

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
    try:
        eventtitle = request.form.get('eventtitle')
    except:
        print("An exception occured")
    print eventtitle
    eventdesc = request.form.get('eventdesc')
    print eventdesc
    starttime = request.form.get('starttime')
    print starttime
    endtime = request.form.get('endtime')
    print endtime

    if endtime < starttime:
        flash('End date and time cannot occur before start date and time. Try again.')
        return redirect(url_for('main.calendar'))

    else:
        new_event = Event(eventtitle=eventtitle, eventdesc=eventdesc, starttime=starttime, endtime=endtime)

        db.session.add(new_event)
        db.session.commit()

        flash('Event successfully added!')
        return redirect(url_for('main.calendar'))
