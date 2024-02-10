from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, TelField, IntegerField, EmailField, SelectField, DateField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
# from models.patient import Patient
from models.user import Role
from config import db_session


class CreaterolesForm(FlaskForm):
    new_role = StringField('Create Role', validators=[DataRequired(), Length(1, 40)])
    create = SubmitField('Create')


class UpdaterolesForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 40), Email()])
    # assign_roles = StringField('Assign Role', validators=[DataRequired(), Length(1, 40)])
    all_roles = db_session.query(Role).all()
    assign_roles = SelectField("Roles", choices=[ role.name for role in all_roles ])

    assign = SubmitField('Assign Role')