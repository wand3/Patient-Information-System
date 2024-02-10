
from flask import request, jsonify, redirect, url_for, render_template, flash
from webapp.api.v1 import api_views
from models.user import User
from config import db_session


@api_views.route('/delete_role/<id>', methods=["POST"], strict_slashes=False)
def admin_delete_user_role(id):
    users = db_session.query(User).all()
    delete_id = db_session.query(User).get(id)
    # user.delete_user_role(user)
    if delete_id:
        if len(delete_id.roles) == 0:
            flash("User does not have any role")      
            return redirect(url_for("admin.base"))
        delete_id.delete_user_role(id=delete_id)
        db_session.commit()
        flash(f"User {delete_id.username}'s Role deleted")      
        return redirect(url_for("admin.base"))
