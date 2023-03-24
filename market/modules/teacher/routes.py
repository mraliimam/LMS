from flask import render_template
from market.modules.teacher import teacher

@teacher.route('/')
@teacher.route('/home')
def home_page():
    return render_template('teacher/teacher.html')