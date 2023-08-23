from flask import render_template
from flask_login import current_user

from app import app


@app.route('/home')
def home():
    return render_template('main.html', current_user=current_user)


@app.route('/registering')
def registering():
    return render_template('registering.html')


@app.route('/login')
def login_user():
    return render_template('login.html')


@app.route('/add_heart_rate')
def add_heart_rate_user():
    return render_template('heart_rate.html')
