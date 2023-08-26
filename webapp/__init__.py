from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from webapp.views import app_views


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.register_blueprint(app_views, url_prefix='/pis')
    db.init_app(app)





    return app