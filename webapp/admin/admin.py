from flask import render_template, url_for, abort, redirect, request, flash
from . import admin
from webapp.admin.forms import CreaterolesForm, UpdaterolesForm
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
    roles = db_session.query(Role).all()
    form_update = UpdaterolesForm()
    email = form_update.email.data
    role_to_assign = form_update.assign_roles.data
    user = db_session.query(User).filter_by(email=email).first()
    if user:
        
        user.add_role_to_user(email=email, role_name=role_to_assign)
        # db_session.commit()
        flash("Role added successfuly")
    return redirect(url_for('admin.base', form_update=form_update, user=user, roles=roles))


# edit users and patients records

# search database with filters of either users and patients
# display count of entire database users and patients
# display doctors and record officers actions and time

@login_required
@has_role('administrator')
@admin.route('/base', methods=["GET", "POST"], strict_slashes=False)
def base():
    form = CreaterolesForm()
    form_update = UpdaterolesForm()
    

    users = db_session.query(User).all()
    roles = db_session.query(Role).all()
    patients = db_session.query(Patient).all()

    return render_template('admin.html', users=users, patients=patients, form=form, roles=roles, form_update=form_update)

