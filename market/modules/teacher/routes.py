from flask import render_template,request, redirect, url_for, flash
from market.modules.teacher import teacher
from market import forms, models
from market.modules import admin
from market.modules.teacher import baseHandler
from flask_login import login_user, logout_user, current_user, login_required
from market.models import roles_required

@teacher.route('/')
@teacher.route('/home')
def home_page():
    return render_template('teacher/home.html')

@teacher.route('/profile')
def profile_page():

    form = forms.TeacherForm()
    tID = request.args.get('tID')
    # tID = current_user.username

    form,image = admin.baseHandler.renderTeacher(form, tID)            
    return render_template('teacher/profile.html', form = form, image = image)

@teacher.route('/courses', methods = ['GET','POST'])
def courses_page():

    if request.method == 'GET':

        # items,cols = baseHandler.getCourses(current_user)
        items,cols = baseHandler.getCourses(None)

        return render_template('teacher/courses.html', items = items, cols = cols)        
    
    if request.method == 'POST':

        act = request.form.get(key = 'act')
        record = admin.baseHandler.con(request.form.get(key = 'record'))

        print(act,record)
        if act == 'attendance':
            print('go')
            return redirect(url_for('teacher.attendance_page', course = record[0], grade = record[2]))            

        elif act == 'progress':
            # return redirect(url_for('teacher.progress_page'))
            pass

        elif act == 'assignment':

            pass

# @teacher.roue('/studentProgress')
# def progress_page():

#     return render_template('teacher.progress.html')

@teacher.route('/assignment')
def assignment_page():

    if request.method == 'GET':

        pass

    elif request.method == 'POST':

        pass

@teacher.route('/attendance', methods = ['GET', 'POST'])
def attendance_page():

    course = request.args.get(key = 'course')
    grade = request.args.get(key = 'grade')

    form = forms.AttendaceForm()
    
    if request.method == 'GET':
        
        # result = baseHandler.checkStudent()
        # return render_template('admin/attendance.html', items = result[0], cols = result[1], form = form)

        if course != None and grade != None:
            result = admin.baseHandler.validateCourseAndStudent(course, grade)
            if not result:
                flash('Input Error: Course and Grade do not matched!!', category='danger')
                return redirect(url_for('teacher.attendance_page'))
            else:
                form.course.data = course
                form.grade.data = grade
                return render_template('admin/attendance.html', items = result[0], cols = result[1], form = form)
        else:
            return render_template('admin/attendance.html',form = form)

    if request.method == 'POST':
        
        crse = request.form.get(key = 'course')
        
        if crse:
            return redirect(url_for('teacher.attendance_page', course = form.course.data, grade = form.grade.data))
        else:
            flag = admin.baseHandler.doAttendance(request, course, grade)

            if not flag:
                flash('Error Occured while saving Attendance. Please Try Again', category='danger')
                return redirect(url_for('teacher.attendance_page', course = course, grade = grade))
            else:
                flash('Attendance Saved Successfully!!', category='success')
                return redirect(url_for('teacher.attendance_page', course = course, grade = grade))        