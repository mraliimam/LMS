from market import db
from market import bcrypt, login_manager
from flask_login import UserMixin
from datetime import datetime, date
from functools import wraps

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def roles_required(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.role not in roles:
                flash("You are not authorized to access this page.", category = "danger")
                return redirect(url_for("home_page"))
            return f(*args, **kwargs)
        return wrapped
    return wrapper

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    role = db.Column(db.String(), nullable = False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Person(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    Person_ID = db.Column(db.String(), nullable = False, unique = True)
    First_Name = db.Column(db.String(), nullable = False)
    Middle_Name = db.Column(db.String())
    Last_Name = db.Column(db.String(), nullable = False)
    Cell_No = db.Column(db.String())
    Email = db.Column(db.String())
    Date_Of_Birth = db.Column(db.Date())
    Gender = db.Column(db.String(), nullable = False)
    Address = db.Column(db.Integer(), nullable = False)

class Address(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    Address_Line_1 = db.Column(db.String(), nullable = False)
    Address_Line_2 = db.Column(db.String(), nullable = False)
    City = db.Column(db.String(), nullable = False)
    State = db.Column(db.String(), nullable = False)
    Zip_Code = db.Column(db.String(), nullable = False)

class Student(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    img = db.Column(db.LargeBinary)
    # Batch_ID = db.Column(db.String(), nullable = False)
    Family_ID = db.Column(db.String(), nullable = False)
    Student_ID = db.Column(db.String(), nullable = False)
    Father = db.Column(db.String())
    Mother = db.Column(db.String())

class Teacher(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    img = db.Column(db.LargeBinary)
    Teacher_ID = db.Column(db.String(), nullable = False)
    Salary = db.Column(db.Integer(), nullable = False)
    Joining_Date = db.Column(db.Date())

class Course(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    Course_ID = db.Column(db.String(), nullable = False, unique = True)
    Name = db.Column(db.String(), nullable = False)
    Grade = db.Column(db.String(), nullable = False)

class Assignment(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    Assignment_ID = db.Column(db.String(), nullable = False, unique = True)
    Name = db.Column(db.String(), nullable = False, unique = True)
    Course_ID = db.Column(db.String(), nullable = False)
    Start_Date = db.Column(db.Date(), nullable = False)
    End_Date = db.Column(db.Date(), nullable = False)
    Total_Marks = db.Column(db.Integer(), nullable = False)

class Student_Assignment(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    Student = db.Column(db.String(), nullable = False)
    Assignment = db.Column(db.String(), nullable = False)
    Submitted_Date = db.Column(db.Date())
    Obtained_Marks = db.Column(db.Integer(), default = 0)

class Student_Progress(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    Student = db.Column(db.String(), nullable = False)
    Grade = db.Column(db.String(), nullable = False)
    Score = db.Column(db.String(), default = '0')

class Teacher_Course(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    Teacher = db.Column(db.String(), nullable = False)
    Course = db.Column(db.String(), nullable = False)
    Active = db.Column(db.Boolean())
    Strength = db.Column(db.Integer(), default = 0)

class Student_Course(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    Student = db.Column(db.String(), nullable = False)
    Course = db.Column(db.String(), nullable = False)
    Active = db.Column(db.Boolean())
    Score = db.Column(db.String(), default = '0')


class Student_Attendance(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    Student = db.Column(db.String(), nullable = False)
    Course = db.Column(db.String(), nullable = False)
    Attendance = db.Column(db.Boolean(), default = False)
    Date_Added = db.Column(db.Date(), nullable = date.today())
    Comments = db.Column(db.String())

db.create_all()