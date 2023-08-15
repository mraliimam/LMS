from flask import render_template, request,redirect, url_for, flash,send_file

from market.modules.student import student
from market.modules import admin
from market import forms
from market.modules.student import baseHandler
from flask_login import login_user, logout_user, current_user, login_required
from market.models import roles_required
from datetime import datetime
from market.forms import Student_AssignmentForm


@student.route('/')
@student.route('/home')
def home_page():
    return render_template('student/home.html')


@student.route('/profile')
def profile_page():

    form = forms.StudentForm()
    sID = request.args.get('sID')
    # tID = current_user.username

    form,image = admin.baseHandler.renderStudent(form, None,sID)            
    return render_template('student/profile.html', form = form, image = image)

@student.route('/courses', methods = ['GET', 'POST'])
def course_page():

    if request.method == 'GET':
        items, cols = baseHandler.getCourses(None)
        return render_template('student/courses.html',items = items, cols = cols)

    elif request.method == 'POST':

        pass


@student.route('/assignment', methods = ['GET', 'POST'])
def assignment_page():
    form=Student_AssignmentForm()
    if request.method == 'GET':

        current_date=datetime.now().date()
        items, cols = baseHandler.getAssignment()
        return render_template('student/assignment.html',form=form,items = items, cols = cols,current_date=current_date)

    if request.method == 'POST':

        if form:
            file = request.files['file']
            message = baseHandler.UploadAssignment(form,file)
            category = 'danger' if 'Error' in message else 'success'
            flash(message, category=category)
            return redirect(url_for('teacher.assignment_page'))

        else:
            flash('Enter valid details in form', category='danger')
            return redirect(url_for('teacher.assignment_page'))

