from flask import render_template, request
from market.modules.student import student
from market.modules import admin
from market import forms
from flask_login import login_user, logout_user, current_user, login_required
from market.models import roles_required

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