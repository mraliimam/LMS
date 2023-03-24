from flask import render_template
from market.modules.student import student

@student.route('/')
@student.route('/home')
def home_page():
    return render_template('student/student.html')