from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError
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


class OrderForm(FlaskForm):
    table = SelectField(label = "Table Name")
    persons = IntegerField(label = "Persons")
    otype = StringField(label = "Order Type")
    submit = SubmitField(label = "Allocate Table")

class LoginForm(FlaskForm):
    username = StringField(label = 'UserName', validators=[DataRequired()])
    password = PasswordField(label = 'Password',validators=[DataRequired()])
    submit = SubmitField(label = 'Submit')