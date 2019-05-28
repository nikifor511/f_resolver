# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect
from __init__ import fl_app, db
from forms import LoginForm, RegistrationForm
# from models import User
import psycopg2
from psycopg2 import Error

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
    if reg_form.validate_on_submit():
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="student511",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="resolver")
            cursor = connection.cursor()
            query_str = "select register_user('" + reg_form.username.data + "', '" + reg_form.password.data + "', " + reg_form.type_select.data + ")"
            print(query_str)
            cursor.execute(query_str)    #"select register_user('Fdddordqw', '121212', 1)")

            rec = cursor.fetchall()
            if rec[0][0] == 1:
                flash('Username is busy')
                print('Username is busy')
            else:
                flash('Thanks for registering')
                return redirect('/index')
            connection.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    return render_template('register.html', form=reg_form)
