from flask import Blueprint

api_views = Blueprint('api_views',
				__name__,
				url_prefix="/api/v1"
				)

# import admin/views to prevent 404 error
from webapp.api.v1.admin.admin import *
from webapp.api.v1.views.views import *


def create_module(app, **kwargs):
	app.register_blueprint(api_views)
	return app
