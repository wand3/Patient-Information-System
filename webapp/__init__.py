from flask import Flask
from webapp.views import app_views


def create_app():
    app = Flask(__name__)

    app.register_blueprint(app_views, url_prefix='/pis')




    return app