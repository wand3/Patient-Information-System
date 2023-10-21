from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from webapp.views import app_views


db = SQLAlchemy()

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

    
    db.init_app(app)
    
    app.register_blueprint(app_views, url_prefix='/')





    return app