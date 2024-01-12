#!/usr/bin/env python3
""" Webapp authenticationview
"""
from flask import Blueprint

# create blueprint for app view 
auth_views = Blueprint('auth_views', __name__)

# import views to prevent 404 error
from webapp.auth.auth import *
