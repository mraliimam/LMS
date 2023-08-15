from market import db, models, forms
import datetime

def getCourses(user):


    items = db.engine.execute(f'''select sc.Course, c.Name, sc.Active,sc.Score from student__course sc
                         join course c on sc.Student = 'std10001' and sc.Active = 1
                         and c.Course_ID = sc.Course;''')

    cols = list(items.keys())
    items = list(items)


    return items, cols

def getAssignment():

    items = db.engine.execute(f'''select a.Assignment_ID,c.Name as Course, a.Name,a.End_Date as Deadline from Assignment a join Course c
    on c.Course_ID=a.Course_ID;''')

    cols = list(items.keys())
    items = list(items)


    return items, cols

def UploadAssignment(form,file):
    assignment = models.Student_Assignment(


        Submitted_Date=datetime.datetime.now(),
        Student="Mubashar",
        Obtained_Marks=form.Total_Marks.data,
        Assignment=file.read()

    )

    db.session.add(assignment)

    try:
        db.session.commit()
        return 'Assignment is Uploaded Successfully!!'
    except:
        db.session.rollback()
        return 'An Error Occured while Uploading the Assignment !!'
