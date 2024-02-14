#!/usr/bin/env python3
""" Webapp view
"""
from flask import Blueprint
from flask_cors import CORS


# create blueprint for app view 
app_views = Blueprint('app_views', __name__)
CORS(app_views)

# import views to prevent 404 error
from webapp.views.pis import *
