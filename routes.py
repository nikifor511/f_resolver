# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect
from __init__ import fl_app
from forms import LoginForm, RegistrationForm
from db_adaptor import DB

@fl_app.route('/')
@fl_app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


@fl_app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        rec = DB.query("select login_user('" + login_form.username.data + "', '" + login_form.password.data + "')")
        if rec[0][0] == 2:
            flash('No such user!')
        elif rec[0][0] == 1:
            flash('Invalid password')
        else:
            # flash('Login ok!')
            return redirect('/resolver')


    return render_template('login.html', title='Sign In', form=login_form)

@fl_app.route('/register', methods=['GET', 'POST'])
def register():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        rec = DB.query("select register_user('" + reg_form.username.data + "', '" + reg_form.password.data + "', " + reg_form.type_select.data + ")")
        if rec[0][0] == 1:
            flash('Choose another username!')
        else:
            flash('Thanks for registering!')
            return redirect('/index')
    return render_template('register.html', form=reg_form)

@fl_app.route('/resolver', methods=['GET', 'POST'])
def resolver():
    rec = DB.query()

    return render_template('resolver.html')
