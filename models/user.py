#!/usr/bin/env python3
"""
Patient Model: create a SQLAlchemy model User
"""
from flask import current_app, flash
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table, Boolean
from datetime import datetime
from models.base_model import BaseModel, Base
from config import db_session
from flask_login import AnonymousUserMixin


roles = Table(
       'role_users',
       Base.metadata,
       Column('user_id', Integer, ForeignKey('users.id')),
       Column('role_id', Integer, ForeignKey('roles.id')),
   )


class Role(Base, BaseModel):
    """Class Role: Database table named role
    Attributes:
    * id, integer primary key
    * name, non-nullable string

    - roles available = [<Role 'default'>, <Role 'doctor'>, <Role 'record_officer'>, <Role 'administrator'>]
    """
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)

    def __init__(self, name):
           self.name = name

    def __repr__(self):
        return '<Role %r>' % self.name
    
class User(Base, BaseModel):
    """Class User: Database table named user
    Attributes:
    * id, integer primary key
    * email, non-nullable string
    * username, non-nullable string
    * password_hash, non-nullable string
    
    """    
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(64), unique=True, index=True)
    firstname = Column(String(64), unique=False, index=True)
    lastname = Column(String(64), unique=False, index=True)
    agree = Column(Boolean, default=True)
    password_hash = Column(String(128))
    roles = relationship("Role", secondary=roles)


    def __init__(self, email, username=""):
        self.email = email
        default = db_session.query(Role).filter_by(name="default").one()
        self.username = username
        self.roles.append(default)

        # add administrator
        if self.email == current_app.config['PIS_ADMIN']:
            admin = Role(name='administrator')
            db_session.add(admin)
            db_session.commit()
            self.roles.append(admin)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    

    def has_role(self, *name):
        for role in self.roles:
            if role.name in name:
                return True
        return False

    # get current user roles 
    # def get_user_role(self):
    #     return self.roles
        # for i in name:
        #     if i in self.roles:
        #         return True
        # return False
    

    # get user by email
    def get_user_id_by_email(self, email):
        # query user table by email and get first result
        user = db_session.query(User).filter_by(email=email).first()
        # if user is found return user ID
        if user:
            return user.id
        return None

    # add role to a user
    def add_role_to_user(self, email, role_name):
        # get user id from email
        user = self.get_user_id_by_email(email)
        # loaded user to assign role to
        add_to_user = db_session.query(User).filter_by(id=user).one()
        new_role = db_session.query(Role).filter_by(name=role_name).first()
        if not new_role:
            new = Role(name=role_name)
            db_session.add(new)
            db_session.commit()
        elif add_to_user:
            existing_row = add_to_user.roles
            existing_row.append(new_role)
            db_session.commit()


    # delete a role from user 
    def delete_user_role(self, id):
        # get user id from email
        user = self.get_id()
        # loaded user to delete role from
        role_delete = db_session.query(User).filter_by(id=user).one()
        users_roles = role_delete.roles
        if user:
            if len(users_roles) > 0:
                users_roles.pop()
                # role_delete.roles.pop()
                db_session.commit()
            flash(f"User has no role at the moment")

        
            


    @property
    def is_active(self):
        return True
    
    @property
    def is_authenticated(self):
        return True
        # if self.user_logged_in:
        #     return True
    
    @property
    def is_anonymous(self):
        return False
        
    
    #fixes user signin route not redirecting if you're not using the UserMixin class
    def get_id(self):
        return (self.id)
    
    def __repr__(self):
        return '<User %r>' % self.username

  
class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False
    
    @property
    def is_anonymous(self):
        return True