from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, TelField, IntegerField, EmailField
from wtforms.validators import DataRequired


class PatientRegForm(FlaskForm):
    fname = StringField( 'First Name', validators=[DataRequired()])
    lname = StringField( 'Last Name', validators=[DataRequired()])
    oname = StringField( 'Other Name(s)', validators=[DataRequired()])
    address = StringField( 'Address', validators=[DataRequired()])
    email = StringField( 'Email', validators=[DataRequired()])
    phone  = IntegerField( 'Phone Number', validators=[DataRequired()])
    mob = IntegerField( 'Month', validators=[DataRequired()])
    yob = IntegerField( 'Year', validators=[DataRequired()])
    gender = StringField( 'Gender', validators=[DataRequired()])
    bloodGroup = StringField( 'Blood Group', validators=[DataRequired()])
    genotype = StringField( 'Genotype', validators=[DataRequired()])
    history = TextAreaField( 'History')
    doctor = StringField('Doctor')
    submit = SubmitField('Register')
