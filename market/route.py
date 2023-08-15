from flask import render_template, redirect, url_for, flash, request
from market import app
from flask_login import login_user, logout_user, current_user, login_required
from market.forms import  LoginForm
from market.modules.admin import baseHandler


@app.route('/')
@app.route('/home')
@login_required
def home_page():
    return render_template('admin/home.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()

    if request.method == 'GET':
        return render_template('temp_templates/login.html', form=form)

    if request.method == 'POST':

        if baseHandler.auth(form) == 'admin':
            flash(f'Welcome {current_user.username}!!', category='success')
            return redirect(request.args.get('next') or url_for('admin.home_page'))
        elif baseHandler.auth(form) == 'teacher':
            flash(f'Welcome {current_user.username}!!', category='success')
            return redirect(request.args.get('next') or url_for('teacher.home_page'))
        elif baseHandler.auth(form) == 'student':
            flash(f'Welcome {current_user.username}!!', category='success')
            return redirect(request.args.get('next') or url_for('student.home_page'))
        else:
            flash('Wrong Username or Password', category='danger')
            return redirect(url_for('login_page'))


@app.route('/logout')
@login_required
def logout_page():
    logout_user()
    flash('User is logout Successfuly!!', category='info')
    return redirect(url_for('login_page'))
