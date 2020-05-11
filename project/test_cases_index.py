from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required

def test_index_pass():
    from .cal.cal import indexCal, index
    indexCal(2020, 8)
    assert index["year"] == 2020

def test_index_fail():
    from .cal.cal import indexCal, index
    indexCal(2010, 8)
    assert index["year"] != 2020
