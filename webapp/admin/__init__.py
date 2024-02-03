from flask import Blueprint

admin_views = Blueprint('admin',
                        __name__,
                        template_folder="../templates/admin",
                        url_prefix="/admin")

# import views to prevent 404 error
from webapp.admin.admin import *

def create_module(app, **kwargs):
    app.register_blueprint(admin_views)