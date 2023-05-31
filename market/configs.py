from market import db
from market import models

db.engine.execute('delete from address;')
db.engine.execute('delete from person;')
db.engine.execute('delete from student;')

def formfill(form):        
    form.sFirstName.data= '1231231'
    form.sMiddleName.data= '1231231'
    form.sLastName.data= '1231231'
    form.sCell_No.data= '1231231'
    form.sEmail.data= '1231231'
    form.dob.data = '2000-01-01'

    #   Address Part
    form.addressLine1.data= '1231231'
    form.addressLine2.data= '1231231'
    form.city.data= '1231231'
    form.state.data= '1231231'
    form.zipCode.data= '1231231'
    
    #   Father
    form.fatherFirstName.data= '1231231'
    form.fatherMiddleName= '1231231'
    form.fatherLastName= '1231231'
    form.fDob.data = '2000-01-01'
    form.FCell_No.data= '1231231'
    form.FEmail.data= '1231231'

    #   Mother
    form.motherFirstName.data= '1231231'
    form.motherMiddleName.data= '1231231'
    form.motherLastName.data= '1231231'
    form.mDob.data = '2000-01-01'
    form.MCell_No.data= '1231231'
    form.MEmail.data = '1231231'

#=============================================

course1 = models.Course(
    Course_ID = "ISL001",
    Name = 'Islamiat',
    Grade = '1'
)

course2 = models.Course(
    Course_ID = "ISL002",
    Name = 'Islamiat',
    Grade = '2'
)

db.session.add(course1)
db.session.add(course2)
db.session.commit()


student1 = models.Student_Course(
    Student = "std10001",
    Course = "ISL001",
    Active = 1
)
db.session.add(student1)

student1 = models.Student_Course(
    Student = "std10002",
    Course = "ISL001",
    Active = 1
)
db.session.add(student1)

student1 = models.Student_Course(
    Student = "std10003",
    Course = "ISL001",
    Active = 1
)
db.session.add(student1)

student2 = models.Student_Course(
    Student = "std10004",
    Course = "ISL002",
    Active = 1
)
db.session.add(student2)

student2 = models.Student_Course(
    Student = "std10005",
    Course = "ISL002",
    Active = 1
)
db.session.add(student2)

db.session.commit()