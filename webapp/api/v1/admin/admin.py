
from flask import request, jsonify, redirect, url_for, render_template
from webapp.api.v1 import api_views
from models.user import User
from config import db_session


@api_views.route('/delete_role/<id>', methods=["GET"], strict_slashes=False)
def admin_delete_user_role(id):
    users = db_session.query(User).all()
    if id in users:
        return jsonify({'message': f'User {id} role deleted!'})

    else: 
        return jsonify({'Message': f'User {id} not found'}), 404
