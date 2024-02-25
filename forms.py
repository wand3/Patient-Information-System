from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, TelField, IntegerField, EmailField, SelectField, DateField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from models.patient import Patient
# from models.user import Role, User
from config import db_session


class SignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 40), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 40), 
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Usernames must have only letters, numbers, dots or '
               'underscores')])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')


class SigninForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log In')


class PatientRegForm(FlaskForm):
    fname = StringField( 'First Name', validators=[DataRequired()])
    lname = StringField( 'Last Name', validators=[DataRequired()])
    oname = StringField( 'Other Name(s)', validators=[DataRequired()])
    address = StringField( 'Address', validators=[DataRequired()])
    email = EmailField( 'Email', validators=[DataRequired()])
    phone  = TelField( 'Phone Number', validators=[DataRequired()])
    dob = DateField( 'Date Of Birth', validators=[DataRequired()], format='%Y-%m-%d')
    gender = SelectField('Gender', choices=['','Female', 'Male'], coerce=str)
    bloodgroup = SelectField( 'Blood Group', choices=['', 'A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'], coerce=str)
    genotype = SelectField( 'Genotype', choices=['', 'AA', 'AS', 'SS'], coerce=str)
    marital_status = SelectField('Marital Status', choices=['', 'Single', 'Married', 'Widowed', 'Divorced', 'Separated'])
    submit = SubmitField('Register')


class UpdatePatientForm(FlaskForm):
    fname = StringField( 'First Name', default=Patient.fname)
    lname = StringField( 'Last Name', default=Patient.lname)
    oname = StringField( 'Other Name(s)', validators=[])
    address = StringField( 'Address', validators=[])
    email = EmailField( 'Email', validators=[])
    phone  = TelField( 'Phone Number', validators=[])
    dob = DateField( 'Date of Birth', validators=[])
    gender = SelectField('Gender', choices=['Female', 'Male'])
    bloodgroup = SelectField( 'Blood Group', choices=['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'])
    genotype = SelectField( 'Genotype', choices=['AA', 'AS', "SS"])
    marital_status = SelectField('Marital Status', choices=['Single', 'Married', 'Widowed', 'Divorced', 'Separated'])
    submit = SubmitField('Update')
