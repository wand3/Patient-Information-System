#!/usr/bin/env python3
"""
Route module for the app
"""
from os import getenv
from webapp import create_app, db
from flask import Flask, jsonify, abort, request
import os
from models.models import Patient

env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('config.%sConfig' % env.capitalize())


"""
returns a dictionary that includes the database instance and the models in which 
flask shell command will import these items automatically into the shell for user
in flask terminal
"""
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Patient=Patient) 



@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def resource_not_found(e):
    """Unauthorized Handler Code: 401"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_app(e):
    """Forbidden Handler Code:403"""
    return jsonify({"error": "Forbidden"}), 403


# @app.before_request
# def before_request():
#     """Before Request Flask"""
#     if auth is not None:
#         pathList = ['/api/v1/status/',
#                     '/api/v1/unauthorized/',
#                     '/api/v1/forbidden/']
#         if auth.require_auth(request.path, pathList) is False:
#             return
#         if auth.authorization_header(request) is None:
#             abort(401)
#         if auth.current_user(request) is None:
#             abort(403)


if __name__ == "__main__":
    # host = getenv("HOST", "0.0.0.0")
    # port = getenv("PORT", "5000")
    # app.run(host=host, port=port)
    app.run(debug=True)
