import calendar

import flask
from flask import render_template
from flask import render_template, Blueprint
from flask_login import login_required, current_user
import datetime
import holidays

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe

calendar_bp = flask.Blueprint('cal', __name__, template_folder='templates')


@calendar_bp.route('/<int:year>/<int:month>')
@login_required
def random_cal(year, month, ev = {}):
    tc = calendar.HTMLCalendar(firstweekday=0)
    tc.cssclasses = ["mon bg-primary", "tue", "wed", "thu", "fri", "sat", "sun"]
    tc.cssclass_month = "table"
    # print(tc.formatmonth(year, month))
    return render_template("calendar.html", calendar=custformat(tc, year, month, ev))

def cal_with_events():
    tc = calendar.HTMLCalendar(firstweekday=0)
    tc.cssclasses = ["mon bg-primary", "tue", "wed", "thu", "fri", "sat", "sun"]


def custformat(c, theyear, themonth, ev, withyear=True):
    """
    Return a formatted month as a table.
    """
    v = []
    a = v.append
    a('<table border="0" cellpadding="0" cellspacing="0" class="%s">' % (
        c.cssclass_month))
    a('\n')
    a(c.formatmonthname(theyear, themonth, withyear=withyear))
    a('\n')
    a(c.formatweekheader())
    a('\n')
    for week in c.monthdays2calendar(theyear, themonth):
        a(custformatweek(c, week, ev))
        a('\n')
    a('</table>')
    a('\n')
    return ''.join(v)


def custformatweek(c, theweek, ev):
    """
    Return a complete week as a table row.
    """
    s = ''.join(custformatday(c, d, wd, ev) for (d, wd) in theweek)
    return '<tr>%s</tr>' % s


def custformatday(c, day, weekday, ev):
    """
    Return a day as a table cell.
    """
    now = datetime.datetime.now()
    if day == 0:
        # day outside month
        return '<td class="%s">&nbsp;</td>' % "noday"
    else:
        return '<td class="%s">%s</td>' % (c.cssclasses[weekday], str(day) + get_event(day, ev))

# TODO do something better than this
def get_event(day, ev):
    if day in ev:
        str = "<div>"
        for event in ev[day]:
            str += event
        str += "</div>"
        return str
    return "<div class='bg-danger'>I'm an event</div>"
    # don't forget you have access to year and month
   # return "<div class='bg-danger'>I'm an event</div>"
   # now = datetime.datetime.now()
   # if day == now.day:
   #     return "<div class='bg-danger'>TODAY</div>"
   # else:
   #     return "<div class='bg-danger'>I'm an event</div>"

#def get_context_data(self, **kwargs):
#    d = get_date(self.request.GET.get('month', None))
#    context['prev_month'] = prev_month(d)
#    context['next_month'] = next_month(d)
#    return context

#def prev_month(d):
#    first = d.replace(day=1)
#    prev_month = first - timedelta(days=1)
#    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
#    return month

#def next_month(d):
#    days_in_month = calendar.monthrange(d.year, d.month)[1]
#    last = d.replace(day=days_in_month)
#    next_month = last + timedelta(days=1)
#    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
#    return month
