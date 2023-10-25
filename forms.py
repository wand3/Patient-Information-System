from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField
from wtf.validators import DataRequired


class PatientRegForm(FlaskForm):
    fname = StringField( 'fname', validators=[DataRequired()])
    lname = StringField( 'lname', validators=[DataRequired()])
    oname = StringField( 'oname', validators=[DataRequired()])
    address = StringField( 'address', validators=[DataRequired()])
    email = StringField( 'email', validators=[DataRequired()])
    phone  = StringField( 'phone', validators=[DataRequired()])
    mob = StringField( 'mob', validators=[DataRequired()])
    yob = StringField( 'yob', validators=[DataRequired()])
    gender = StringField( 'gender', validators=[DataRequired()])
    bloodGroup = StringField( 'bloodGroup', validators=[DataRequired()])
    genotype = StringField( 'genotype', validators=[DataRequired()])
    history = TextField( 'history', validators=[DataRequired()])
    doctor = StringField( 'doctor', validators=[DataRequired()])
