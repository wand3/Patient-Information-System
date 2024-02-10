
from flask import request, jsonify, redirect, url_for, render_template
from webapp.api.v1 import api_views
from models.user import User
from config import db_session


@api_views.route('/delete_role/<id>', methods=["POST"], strict_slashes=False)
def admin_delete_user_role(id):
    users = db_session.query(User).all()
    delete_id = db_session.query(User).get(id)
    # user.delete_user_role(user)
    if delete_id:
        delete_id.delete_user_role(id=delete_id)
        db_session.commit()
        return jsonify({'message': f'User {id} role deleted!'})
    else: 
        db_session.roll_back()
        return jsonify({'Message': f'User {id} not found'}), 404
    

    # db_session.commit()



    # for u in user:
    #     if id == user.id:
    #         return jsonify({'message': f'User {id} role deleted!'})

    #     else: 
    #         return jsonify({'Message': f'User {id} not found'}), 404
        
