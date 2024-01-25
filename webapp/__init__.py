from flask import Flask
from webapp.views import app_views


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
        
    app.register_blueprint(app_views, url_prefix='/')

    from webapp.auth import create_module as auth_create_module
    auth_create_module(app)



    return app