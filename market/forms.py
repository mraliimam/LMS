from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, SelectField, EmailField, DateField, FileField
from wtforms.validators import DataRequired, Length, ValidationError, Email, Regexp
from flask_wtf.file import FileAllowed, FileSize
from market.models import Student, Course
from market import db
from flask import flash


# class MedicineForm(FlaskForm):

#     def mrn_func(self):
#         for i in Medicine.query.filter_by(Status = "IN"):
#             pass
        
#         try:
#             m = i.Batch_ID
#             m = m[3:]
#             m = int(m)
#             m += 1
#             m = 'med'+str(m)
#             return m
#         except:
#             m = 'med1'
#             return m

#     def validate_sales(self, sales_to_check):
#         if sales_to_check.data < self.purchase.data:
#             flash("Sales Price cannot be less than Purchase Price!! Try Again..", category='danger')
#             raise ValidationError('Sales Price cannot be less than Purchase Price!! Try Again..')
            
#         else:
#             pass

#     id = StringField(label = 'Batch ID', validators= [DataRequired()])
#     cName = StringField(label = 'Product Name',validators= [Length(min=3), DataRequired()])
#     gName = StringField(label = 'Supplier Name',validators= [Length(min=3), DataRequired()])
#     date = DateField(label = "Date Added", validators=[DataRequired()])
#     expiry = DateField(label = 'Expiry Date', validators= [DataRequired()])
#     entry = IntegerField(label= 'Stock Qty', validators=[DataRequired()])
#     purchase = FloatField(label=  'Purchase Price', validators=[DataRequired()])
#     sales = FloatField(label=  'Sale Price', validators=[DataRequired()])
#     market = FloatField(label=  'Market Price', validators=[DataRequired()])
#     subsidy = FloatField(label = 'Subsidy', validators=[DataRequired()])
#     submit = SubmitField(label = 'Submit Medicine')


class StudentForm(FlaskForm):

    def stID(self):
        for i in Student.query.all():
            pass
        
        try:
            m = i.Student_ID
            m = m[3:]
            m = int(m)
            m += 1
            m = 'std'+str(m)
            return m
        except:
            m = 'std10001'
            return m
    
    def famID(self):
        for i in Student.query.all():
            pass
        
        try:
            m = i.Family_ID
            m = m[3:]
            m = int(m)
            m += 1
            m = 'fam'+str(m)
            return m
        except:
            m = 'fam10001'
            return m

    def fatherID(self):
        for i in Student.query.all():
            pass

        try:
            m = i.Father
            m = m[6:]
            m = int(m)
            m += 1
            m = 'father'+str(m)
            return m
        except:
            m = 'father10001'
            return m

    def motherID(self):
        for i in Student.query.all():
            pass

        try:
            m = i.Mother
            m = m[6:]
            m = int(m)
            m += 1
            m = 'mother'+str(m)
            return m
        except:
            m = 'mother10001'
            return m

    # familyID = SelectField(label = 'Family ID', validators=[DataRequired()])
    familyID = StringField(label = 'Family ID', validators=[DataRequired()])

    # sImg = FileField(label='Student Profile Image', validators=[
    #     FileAllowed(['jpg', 'jpeg', 'png'], 'Only JPEG and PNG images are allowed!'),
    #     FileSize(max_size=3 * 1024 * 1024, message='Image must be under 3MB!')
    # ])
    sID = StringField(label = 'Student ID', validators=[DataRequired()])
    sFirstName = StringField(label = 'First Name', validators=[DataRequired()])
    sMiddleName = StringField(label = 'Middle Name', validators=[DataRequired()])
    sLastName = StringField(label = 'Last Name', validators=[DataRequired()])
    sCell_No = StringField(label = 'Phone No', validators=[Regexp(r'^\([2-9]{1}[0-9]{2}\)\ [2-9]{1}[0-9]{2}-[0-9]{4}$', message="Invalid phone number format")])
    sEmail = EmailField(label = 'Email', validators=[Email(message='Invalid Email type')])
    dob = DateField(label = 'Date of Birth', validators=[DataRequired()])
    gender = SelectField(label = 'Gender', choices=['Male','Female'], validators=[DataRequired()])

    #   Address Part
    addressLine1 = StringField(label='Address Line 1')
    addressLine2 = StringField(label='Address Line 2')
    city = StringField(label='City')
    state = StringField(label='State')
    zipCode = StringField(label='Zip Code')
    
    #   Father
    fatherFirstName = StringField(label = 'First Name', validators=[DataRequired()])
    fatherMiddleName = StringField(label = 'Middle Name', validators=[DataRequired()])
    fatherLastName = StringField(label = 'Last Name', validators=[DataRequired()])
    fDob = DateField(label = 'Date of Birth', validators=[DataRequired()])
    FCell_No = StringField(label = 'Phone No', validators=[Regexp(r'^\([2-9]{1}[0-9]{2}\)\ [2-9]{1}[0-9]{2}-[0-9]{4}$', message="Invalid phone number format")])
    FEmail = EmailField(label = 'Email', validators=[Email(message='Invalid Email type')])

    #   Mother
    motherFirstName = StringField(label = 'First Name', validators=[DataRequired()])
    motherMiddleName = StringField(label = 'Middle Name', validators=[DataRequired()])
    motherLastName = StringField(label = 'Last Name', validators=[DataRequired()])
    mDob = DateField(label = 'Date of Birth', validators=[DataRequired()])
    MCell_No = StringField(label = 'Phone No', validators=[Regexp(r'^\([2-9]{1}[0-9]{2}\)\ [2-9]{1}[0-9]{2}-[0-9]{4}$', message="Invalid phone number format")])
    MEmail = EmailField(label = 'Email', validators=[Email(message='Invalid Email type')])

    submit = SubmitField(label = 'Submit')

class LoginForm(FlaskForm):
    username = StringField(label = 'UserName', validators=[DataRequired()])
    password = PasswordField(label = 'Password',validators=[DataRequired()])
    submit = SubmitField(label = 'Submit')


class AttendaceForm(FlaskForm):
    course = SelectField(label = 'Subject', validators=[DataRequired()], choices=[i.Name for i in Course.query.all()])
    grade = SelectField(label = 'Grade', validators=[DataRequired()], choices=[i.Grade for i in Course.query.all()])
    submit = SubmitField(label = 'Submit')