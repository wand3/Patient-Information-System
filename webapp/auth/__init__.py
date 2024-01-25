#!/usr/bin/env python3
""" Webapp authenticationview
"""
import functools
from flask import Blueprint, abort
from models.user import User
from config import db_session
from flask_login import LoginManager, current_user

# create blueprint for auth views 
auth_views = Blueprint('auth_views', __name__, template_folder='../templates/auth',
    url_prefix="/auth")


login_manager = LoginManager()
login_manager.login_view = 'signin'
login_manager.session_protection = "basic"
login_manager.login_message = "Please login to access this page"
login_manager.login_message_category = "info"


def create_module(app, **kwargs):
    login_manager.init_app(app)
    app.register_blueprint(auth_views)

# import views to prevent 404 error
from webapp.auth.auth import *

def has_role(name):
    def real_decorator(f):
        def wraps(*args, **kwargs):
            if current_user.has_role(name):
                return f(*args, **kwargs)
            else:
                abort(403)
        return functools.update_wrapper(wraps, f)
    return real_decorator


@login_manager.user_loader
def load_user(id):
    return db_session.query(User).get(id)