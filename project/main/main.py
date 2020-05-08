from flask import render_template, Blueprint, redirect, url_for, request
from flask_login import login_required, current_user
import datetime
from ..cal.cal import random_cal
from ..models import Event
from ..app import db

main_bp = Blueprint('main', __name__)

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
    return random_cal(now.year, now.month,{
        1: ["example"],
        8: ["no."],
        19: ["bye."]
    })

@main_bp.route("/calendar", methods=['POST'])
def events():
    eventtitle = request.form.get('event title')
    eventdesc = request.form.get('event description')
    starttime = request.form.get('start day/start time')
    endtime = request.form.get('end day/end time')

    new_event = Event(eventtitle=eventtitle, eventdesc=eventdesc, starttime=starttime, endtime=endtime)

    db.session.add(new_event)
    db.session.commit()

    flash('Event successfully added.')
    return redirect(url_for('main.calendar'))
