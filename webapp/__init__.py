from flask import Flask
from webapp.views import app_views
from webapp.auth import auth_views
from flask_login import LoginManager
from config import db_session
from models.user import User


login_manager = LoginManager()
login_manager.login_view = 'auth_views.signin'


def create_app(object_name):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
        e.g. Patient-Information-System.config.DevConfig
    """
    app = Flask(__name__)
    import config
    app.config.from_object(object_name)

    login_manager.init_app(app)
    
    app.register_blueprint(app_views, url_prefix='/')
    app.register_blueprint(auth_views, url_prefix='/auth')


    return app

@login_manager.user_loader
def load_user(id):
    return db_session.get(User, int(id))
