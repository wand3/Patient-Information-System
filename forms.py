from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, TelField, IntegerField, EmailField, SelectField
from wtforms.validators import DataRequired
from models.patient import Patient
from config import db_session

class PatientRegForm(FlaskForm):
    fname = StringField( 'First Name', validators=[DataRequired()])
    lname = StringField( 'Last Name', validators=[DataRequired()])
    oname = StringField( 'Other Name(s)', validators=[DataRequired()])
    address = StringField( 'Address', validators=[DataRequired()])
    email = EmailField( 'Email', validators=[DataRequired()])
    phone  = TelField( 'Phone Number', validators=[DataRequired()])
    mob = IntegerField( 'Month', validators=[DataRequired()])
    yob = IntegerField( 'Year', validators=[DataRequired()])
    gender = SelectField('Gender', choices=['','Female', 'Male'], coerce=str)
    bloodgroup = SelectField( 'Blood Group', choices=['', 'A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'], coerce=str)
    genotype = SelectField( 'Genotype', choices=['', 'AA', 'AS', 'SS'], coerce=str)
    doctor = StringField('Doctor')
    submit = SubmitField('Register')


class UpdatePatientForm(FlaskForm):
    # patient = db_session.get(Patient.id, id)
    fname = StringField( 'First Name', default=Patient.fname)
    lname = StringField( 'Last Name', default=Patient.lname)
    oname = StringField( 'Other Name(s)', validators=[])
    address = StringField( 'Address', validators=[])
    email = EmailField( 'Email', validators=[])
    phone  = TelField( 'Phone Number', validators=[])
    mob = IntegerField( 'Month', validators=[])
    yob = IntegerField( 'Year', validators=[])
    gender = SelectField('Gender', choices=['Female', 'Male'], coerce=str)
    bloodgroup = SelectField( 'Blood Group', choices=['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'], coerce=str)
    genotype = SelectField( 'Genotype', choices=['AA', 'AS', 'SS'], coerce=str)
    doctor = StringField('Doctor')
    submit = SubmitField('Update')
