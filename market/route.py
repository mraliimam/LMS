from flask import render_template, redirect, url_for, flash, request
from market import app

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('admin/home.html')