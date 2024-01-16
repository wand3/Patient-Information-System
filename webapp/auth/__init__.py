#!/usr/bin/env python3
""" Webapp authenticationview
"""
import functools
from flask import Blueprint, abort
from models.user import User
from config import db_session


# create blueprint for app view 
auth_views = Blueprint('auth_views', __name__)

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