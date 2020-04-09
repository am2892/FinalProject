from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

new_user = User(email='test@test.com', name='test', password='1234')
existing_user = User(email='test@dummy.com', name='test', password='1234')

def test_login():
    from project.auth import login_post
    #assert login_post(email, password, remember, user) == redirect(url_for('main.profile'))

#def test_login_fail():

def test_logout():
    from project.auth import logout
    render_template('/login.html')
    assert logout == redirect(url_for('main.index'))

#def test_logout_fail():

def test_signup():
    from project.auth import signup_post
    #Success Test:
    assert new_user.email == 'test@test.com'
    #Fail Test:
    assert signup_post != 'Email address already exsits'

def test_login_dummy():
    from project.auth import login_post
#    assert login_post == redirect(url_for('main.profile'))
