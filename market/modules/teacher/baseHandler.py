from market import db, models, forms
import datetime
from flask import send_file
from market.models import Assignment
import os,io



def createAssignmentID(form):


    form.A_ID.data = forms.AssignmentForm().assignmentID()
    form.A_ID.render_kw = {'readonly':True}



    return form
def getCourses(user):
    
    # items = db.engine.execute(f'''select c.Name, c.Grade, tc.Strength from teacher_course tc
    #                      join course c on tc.Teacher = '{user.username}' and tc.Active = 1;''')
    items = db.engine.execute(f'''select c.Course_ID, c.Name, c.Grade, tc.Strength from teacher__course tc
                         join course c on tc.Teacher = 'tr10001' and tc.Active = 1
                         and c.Course_ID = tc.Course;''')

    cols = list(items.keys())
    items = list(items)

    return items,cols

def CreateAssignment(form,file):

    assignment= models.Assignment(
        Assignment_ID=form.A_ID.data,
        Name=form.Name.data,
        Course_ID=form.Course_ID.data,
        Start_Date=datetime.datetime.now(),
        End_Date=form.End_Date.data,
        Total_Marks=form.Total_Marks.data,
        file = file.read()

    )

    db.session.add(assignment)


    try:
        db.session.commit()
        return 'Assignment is Uploaded Successfully!!'
    except:
        db.session.rollback()
        return 'An Error Occured while Uploading the Assignment !!'


def getAssignment():

    items = db.engine.execute(f'''select a.Assignment_ID,a.Course_ID, a.Name,a.End_Date as Deadline from Assignment a;''')

    cols = list(items.keys())
    items = list(items)


    return items, cols

def get_assignment_file(Assignment_ID):
    assignment_result = db.engine.execute(
        f'''SELECT * FROM Assignment WHERE Assignment_ID = '{Assignment_ID}';''')
    assignment = assignment_result.fetchone()

    if assignment:
        file_data = assignment['file']
        if file_data:
            extension = os.path.splitext(".")[1]  # Extract extension
            return send_file(io.BytesIO(file_data), as_attachment=True, download_name=f"{Assignment_ID}{extension}")
        else:
            return "File not found"
    else:
        return "Assignment not found"
