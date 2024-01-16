#!/usr/bin/env python3
"""
Patient Model: create a SQLAlchemy model User
"""
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from datetime import datetime
from models.base_model import BaseModel, Base
from config import db_session

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
    username = Column(String(64), unique=True, index=True)
    password_hash = Column(String(128))
    roles = relationship("Role", secondary=roles)


    def __init__(self, email, username="" ):
        self.email = email
        # super(User, self).__init__(**kwargs)
        # def __init__(self, username=""):
        default = db_session.query(Role).filter_by(name="default").one()
        self.roles.append(default)
        self.username = username
        # if self.role is None:
        #     if self.email == current_app.config['PIS_ADMIN']:
        #         self.role = Role.query.filter_by(name='administrator').first()
        #     if self.role is None:
        #         self.role = Role.query.filter_by(default=True).first()

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def has_role(self, name):
        for role in self.roles:
            if role.name == name:
                return True
        return False
    
    @property
    def is_active(self):
        return True
    
    def __repr__(self):
        return '<User %r>' % self.username
    

