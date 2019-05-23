# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect
from __init__ import fl_app
from forms import LoginForm, RegistrationForm
from models import *

@fl_app.route('/')
@fl_app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


@fl_app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.remember_me.data == True:
            # flash('Login requested for user {}, remember_me={}'.format(
            # form.username.data, form.remember_me.data))
            flash('true')
        else:
            flash('false')
        # return redirect('/index')
    return render_template('login.html', title='Sign In', form=login_form)

@fl_app.route('/register', methods=['GET', 'POST'])
def register():
    reg_form = RegistrationForm()
    if reg_form.validate():
        user = User(reg_form.username.data, reg_form.email.data,
                    reg_form.password.data)
        db.add(user)
        flash('Thanks for registering')
        return redirect('/index')
    return render_template('register.html', form=reg_form)
