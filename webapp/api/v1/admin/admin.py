
from flask import request, jsonify
from webapp.api.v1 import api_views

@api_views.route('/', methods=["GET"], strict_slashes=False)
def delete_user_role():
    return '<h1>check</h1>'
