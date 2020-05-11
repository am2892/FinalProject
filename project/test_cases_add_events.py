from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
#from models import User
#from ..app import db

def test_add_event_pass():
    from .main.main import events_post
    from .cal.cal import random_cal
    import datetime
    from datetime import date
    now = datetime.datetime.now()
    ### good data ###
    userName = 'Test User'
    eventtitle = 'Test Title'
    starttime = '2014-04-09 09:30:00'
    endtime = '2020-04-20 09:30:00'
    assert isinstance(userName, str) is True ## check to make sure there is data in userName
    assert isinstance(eventtitle, str) is True ## check to make sure there is data in event title

#    assert starttime ## check to make sure you have a valid start date/time
#    assert endtime ## check to make sure you had a valid end date/time

def test_add_event_fail():
    from .main.main import events_post
    from .cal.cal import random_cal
    import datetime
    from datetime import date
    now = datetime.datetime.now()
    ### bad data ###
    userName = []
    eventtitle = []
    starttime = '204-04-09 09:0:00'
    endtime = '20-0-20 09:0:00'
    assert isinstance(userName, str) is False ## check to make sure there is data in userName
    assert isinstance(eventtitle, str) is False ## check to make sure there is data in event title

#    assert starttime ## check to make sure you have a valid start date/time
#    assert endtime ## check to make sure you had a valid end date/time
