#!/usr/bin/env python3
"""
Patient Model: create a SQLAlchemy model User
"""
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime
from models.base_model import BaseModel, Base
from config import db_session
from webapp import login_manager



class Role(Base, BaseModel):
    """Class Role: Database table named role
    Attributes:
    * id, integer primary key
    * name, non-nullable string
    * user, non-nullable string
    """
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    users = relationship('User', backref='role', lazy='dynamic')


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
    role_id = Column(Integer, ForeignKey('roles.id'))
    password_hash = Column(String(128))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
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
    
    def __repr__(self):
        return '<User %r>' % self.username


@login_manager.user_loader
def load_user(id):
    return db_session.get(User, int(id))