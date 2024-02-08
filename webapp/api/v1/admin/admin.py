
from flask import request, jsonify
from webapp.api.v1 import v1


@v1.route('/', methods=["DELETE"], strict_slashes=False)
def delete_user_role():
    return '<h1>check</h1>'
