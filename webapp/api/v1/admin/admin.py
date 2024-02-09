
from flask import request, jsonify, redirect, url_for
from webapp.api.v1 import api_views
from models.user import User
from config import db_session


@api_views.route('/admin_delete_user_role/<int: id>', methods=["DELETE"], strict_slashes=False)
def admin_delete_user_role(id):
    users = db_session.query(User).all()


    return redirect(url_for('admin.base', users=users))
