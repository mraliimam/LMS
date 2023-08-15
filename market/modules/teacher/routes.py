from flask import render_template,request, redirect, url_for, flash,send_file
from market.modules.teacher import teacher
from market import forms, models
from market.modules import admin
from market.modules.teacher import baseHandler
from market.forms import AssignmentForm
from flask_login import login_user, logout_user, current_user, login_required
from market.models import Assignment
from market import db
from io import BytesIO

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


@teacher.route('/download_assignment/<string:Assignment_ID>', methods=['GET'])
def download_assignment(Assignment_ID):
    file_response  = baseHandler.get_assignment_file(Assignment_ID)
    if file_response:
        return file_response
    else:

        flash('Assignment or file not found', category='danger')
        return redirect(url_for('teacher.assignment_page'))



@teacher.route('/assignment', methods = ['GET', 'POST'])
def assignment_page():
    form = AssignmentForm()
    if request.method == 'GET':


        form = baseHandler.createAssignmentID(form)
        items, cols = baseHandler.getAssignment()
        



        return render_template('teacher/assignment.html', form=form, image = None,items=items,cols=cols)

    if request.method == 'POST':
        form_type=request.form.get('form_type')

        if form_type == 'show':
            if form:
                file = request.files['file']
                message = baseHandler.CreateAssignment(form,file)
                category = 'danger' if 'Error' in message else 'success'
                flash(message, category = category)
                return redirect(url_for('teacher.assignment_page'))

            else:
                flash('Enter valid details in form', category='danger')
                return redirect(url_for('teacher.assignment_page'))

        if form_type == 'update':

            End_Date = request.form['End_Date']
            Assignment_ID = request.form['id']

            date_to_update = Assignment.query.get_or_404(Assignment_ID)

            date_to_update.End_Date = End_Date
            try:
                db.session.commit()

                flash(f"Date of  {Assignment_ID} Updated!", category='success')
            except:
                flash(f"Date of {Assignment_ID} not Updated!", category='danger')

        return redirect(url_for('teacher.assignment_page'))


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

@teacher.route('/update_assignment/<string:id>',methods=['GET','POST'])
def update_assignment(id):

    pass

