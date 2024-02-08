from flask import Blueprint

v1 = Blueprint( 'v1',
				__name__,
				url_prefix="/api/v1"
				)

# import views to prevent 404 error
from webapp.api.v1 import *

def create_module(app, **kwargs):
	app.register_blueprint(v1)
	return app
