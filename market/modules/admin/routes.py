from flask import render_template, request, redirect, flash, url_for
from market.modules.admin import admin
from market.forms import StudentForm, AttendaceForm, TeacherForm
from market.modules.admin import baseHandler
from flask_login import login_user, logout_user, current_user, login_required
from market.models import roles_required

@admin.route('/')
@admin.route('/home')
def home_page():
    form = StudentForm()
    return render_template('admin/home.html', form = form)

@admin.route('/StudentInformation', methods = ['GET', 'POST'])
def student_page():

    if request.method == 'GET':
        items,cols = baseHandler.getStudent()
        return render_template('admin/studentData.html', items = items, cols = cols)

    if request.method == 'POST':
        
        famID = request.form.get(key = 'studentFamily') 
        stdID = request.form.get(key = 'studentID')
        act = request.form.get(key = 'action') 

        if act == 'View':
            return redirect(url_for('admin.reg_student', famID = famID, stdID = stdID))

        return redirect(url_for('admin.reg_student', famID = famID))


@admin.route('/StudentForm', methods = ['GET', 'POST'])
def reg_student():

    form = StudentForm()

    if request.method == 'GET':

        famID = request.args.get('famID')
        stdID = request.args.get('stdID')
        
        form = baseHandler.createFamilyID(form)

        if stdID:
            form,image = baseHandler.renderStudent(form, famID, stdID)            
            return render_template('admin/registerStudent.html', form = form, image = image)
        elif (not stdID) and famID:
            form = baseHandler.renderStudent(form, famID, None)
        
        return render_template('admin/registerStudent.html', form = form, image = None)

    if request.method == 'POST':

        if form.fatherFirstName.data == None:
            return redirect(url_for('admin.reg_student', famID = form.familyID.data))

        elif form:
            file = request.files['file']

            message = baseHandler.createStudent(form, file)
            category = 'danger' if 'Error' in message else 'success'
            flash(message, category = category)
            return redirect(url_for('admin.home_page'))

        else:
            flash('Enter valid details in form', category='danger')
            return redirect(url_for('admin.reg_student'))

@admin.route('/attendance', methods = ['GET', 'POST'])
def attendance_page():

    course = request.args.get(key = 'course')
    grade = request.args.get(key = 'grade')

    form = AttendaceForm()
    
    if request.method == 'GET':
        
        # result = baseHandler.checkStudent()
        # return render_template('admin/attendance.html', items = result[0], cols = result[1], form = form)

        if course != None and grade != None:
            result = baseHandler.validateCourseAndStudent(course, grade)
            if not result:
                flash('Input Error: Course and Grade do not matched!!', category='danger')
                return redirect(url_for('admin.attendance_page'))
            else:
                form.course.data = course
                form.grade.data = grade
                return render_template('admin/attendance.html', items = result[0], cols = result[1], form = form)
        else:
            return render_template('admin/attendance.html',form = form)

    if request.method == 'POST':
        
        crse = request.form.get(key = 'course')
        
        if crse:
            return redirect(url_for('admin.attendance_page', course = form.course.data, grade = form.grade.data))
        else:
            flag = baseHandler.doAttendance(request, course, grade)

            if not flag:
                flash('Error Occured while saving Attendance. Please Try Again', category='danger')
                return redirect(url_for('admin.attendance_page', course = course, grade = grade))
            else:
                flash('Attendance Saved Successfully!!', category='success')
                return redirect(url_for('admin.attendance_page', course = course, grade = grade))        
        

@admin.route('/TeacherForm', methods = ['GET', 'POST'])
def reg_teacher():

    form = TeacherForm()

    if request.method == 'GET':
        
        tID = request.args.get('tID')
        
        form = baseHandler.createTeacherID(form)

        if tID:
            form,image = baseHandler.renderTeacher(form, tID)            
            return render_template('admin/registerTeacher.html', form = form, image = image)
        
        return render_template('admin/registerTeacher.html', form = form, image = None)

    if request.method == 'POST':

        if form:
            file = request.files['file']

            message = baseHandler.createTeacher(form, file)
            category = 'danger' if 'Error' in message else 'success'
            flash(message, category = category)
            return redirect(url_for('admin.home_page'))

        else:
            flash('Enter valid details in form', category='danger')
            return redirect(url_for('admin.reg_teacher'))

@admin.route('/Courses', methods = ['GET', 'POST'])
def course_page():

    if request.method == 'GET':

        pass

    elif request.method == 'POST':

        pass

    pass