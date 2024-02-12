
from flask import request, jsonify, redirect, url_for, render_template, flash
from webapp.api.v1 import api_views
from models.user import User
from config import db_session
from webapp.auth import has_role
from flask_login import login_required


# delete user role


# delete role from a particular user 
@login_required
@api_views.route('/delete_role/<id>', methods=["POST"], strict_slashes=False)
@has_role('administrator')
def admin_delete_user_role(id):
    users = db_session.query(User).all()
    delete_id = db_session.query(User).get(id)
    if delete_id:
        if len(delete_id.roles) == 0:
            flash("User does not have any role")      
            return redirect(url_for("admin.base"))
        delete_id.delete_user_role(id=delete_id)
        db_session.commit()
        flash(f"User {delete_id.username}'s Role deleted")      
        return redirect(url_for("admin.base"))
