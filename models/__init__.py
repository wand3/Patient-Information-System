# import os
from models.base_model import BaseModel
from models.history import History
from models.patient import Patient


# """
#     Database configuration to run WEBAPP_ENV (dev, test, prod) with respect to 
#     classes (DevConfig ,TestConfig, ProdConfig) in config module
# """
# # ENV_CONFIG = os.environ.get('WEBAPP_ENV')
# # import config
# # CNC = config.Config.CNC
# # if ENV_CONFIG == 'test':
# #     storage = config.TestConfig()
# # elif ENV_CONFIG == 'prod':
# #     storage = config.ProdConfig()
# # else:
# #     storage = config.DevConfig()
# # storage.reload()


# # from flask import Flask, render_template, make_response
# # app = Flask(__name__)

# # @app.route('/user/xml')
# # def user_xml():
# #     resp = make_response(render_template('xml/user.html', username='Ryan'))
# #     resp.headers['Content-type'] = 'text/xml; charset=utf-8'
# #     return resp
