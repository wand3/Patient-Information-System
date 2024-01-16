from flask import Flask, render_template, url_for, flash, redirect, request, make_response
from webapp.auth import auth_views
from forms import SigninForm, SignupForm
from config import db_session
from flask_login import current_user
from datetime import datetime
# from ..auth import has_role
from flask_login import login_user, logout_user
from models.user import User
from werkzeug.security import generate_password_hash



@auth_views.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        new_user = User(
            email=form.email.data,
            username=form.username.data,
            )
        new_user.password_hash = generate_password_hash(form.password.data)
        db_session.add(new_user)
        db_session.commit()

        flash("Your user has been created, please login.", category="success")

        return redirect(url_for('.signin'))
    return render_template('auth/signup.html', form=form)


@auth_views.route('/signin', methods=['GET', 'POST'], strict_slashes=False)
def signin():
    form = SigninForm()        
    user = db_session.query(User).filter_by(email=form.email.data).one()
    if form.validate_on_submit():
        if user is not None and user.verify_password(form.password.data):
            login_user(user, remember=form.remember.data)
            # next = request.args.get('next')
            # if next is None or not next.startswith('/'):
            #     next = url_for('.index')
            # return redirect(next)
            return redirect(url_for('index'))



        flash("You have been logged in.", category="success")
    flash('Invalid username or password.')

    return render_template('auth/signin.html', form=form)