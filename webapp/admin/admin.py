from flask import render_template, url_for, abort, redirect
from . import admin_views
from models.base_model import BaseModel
from models.history import History
from models.patient import Patient
from models.user import Role, User
from flask_login import login_required
from webapp.auth import has_role
from config import db_session


@login_required
@has_role('administrator')
@admin_views.route('/base', methods=["GET", "POST"], strict_slashes=False)
def base():
    users = db_session.query(User).all()
    patients = db_session.query(Patient).all()

    return render_template('admin.html', users=users, patients=patients)
