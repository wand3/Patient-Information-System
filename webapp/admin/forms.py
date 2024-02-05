from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, TelField, IntegerField, EmailField, SelectField, DateField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from models.patient import Patient
# from models.user import Role, User
from config import db_session


class CreaterolesForm(FlaskForm):
    new_role = StringField('Create Role', validators=[DataRequired(), Length(1, 40)])
    create = SubmitField('Create')


class UpdaterolesForm(FlaskForm):
    user_email = SelectField('Email', validators=[DataRequired(), Email()])
    assign_roles = StringField('Assign Role', validators=[DataRequired(), Length(1, 40)])
    assign = SubmitField('Assign Role')