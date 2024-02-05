from flask import render_template, url_for, abort, redirect, request
from . import admin
from webapp.admin.forms import CreaterolesForm
from models.base_model import BaseModel
from models.history import History
from models.patient import Patient
from models.user import Role, User
from flask_login import login_required, current_user
from webapp.auth import has_role
from config import db_session


# create roles to users
@login_required
@has_role('administrator')
@admin.route('/create_role', methods=["GET", "POST"], strict_slashes=False)
def create_role():
    form = CreaterolesForm()
    # role = db_session.query(Role)
    if form.validate_on_submit():
        new_role = Role(name=form.new_role.data)
        db_session.add(new_role)
        db_session.commit()
        
    return render_template('base.html', form=form)

# assign roles to users
@login_required
@has_role('administrator')
@admin.route('/assign_role', methods=["GET", "POST"], strict_slashes=False)
def assign_role():
    form = CreaterolesForm()
    # user = db_session.query(User).filter_by(id=current_user.id)
    user = db_session.get(User, id=current_user.id)

    if form.validate_on_submit():
        # new_role = User(id=form.new_role.data)
        existing_row = user.roles
        existing_row.append(form.new_role.data)
        db_session.add(existing_row)
        db_session.commit()
        
    return render_template('base.html', form=form)


# edit users and patients records

# search database with filters of either users and patients
# display count of entire database users and patients
# display doctors and record officers actions and time

@login_required
@has_role('administrator')
@admin.route('/base', methods=["GET", "POST"], strict_slashes=False)
def base():
    form = CreaterolesForm()
    

    users = db_session.query(User).all()
    roles = db_session.query(Role).all()
    patients = db_session.query(Patient).all()

    return render_template('admin.html', users=users, patients=patients, form=form, roles=roles)

