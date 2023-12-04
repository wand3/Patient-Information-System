
from flask import Flask, render_template, url_for, flash, redirect, request, make_response
from webapp.views import app_views
from models.patient import Patient
from forms import PatientRegForm, UpdatePatientForm
from sqlalchemy import update
from config import db_session
from flask_login import current_user
from datetime import datetime


@app_views.route('/', methods=['GET'], strict_slashes=False)
def index():
    all = db_session.query(Patient)
    return render_template("index.html", all=all)


# Patient Registeration route
@app_views.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    form = PatientRegForm(request.form)
    if form.validate_on_submit():
        """
            Override if you need field-level validation. Runs before any other
            validators.

            :param form: The form the field belongs to.
        """
        new_patient = Patient( 
                        fname=form.fname.data, 
                        lname=form.lname.data,
                        oname=form.oname.data,
                        address=form.address.data,
                        email=form.email.data,
                        phone=form.phone.data,
                        mob=form.mob.data,
                        yob=form.yob.data,
                        gender=form.gender.data,
                        bloodgroup=form.bloodgroup.data,
                        genotype=form.genotype.data,
                        doctor=form.doctor.data,
                        )
        db_session.add(new_patient)
        db_session.commit()
        db_session.close()
        flash('Thanks for registering')
        return redirect(url_for('app_views.index'))
    return render_template("register.html", form=form)

# search patient
# @app_views.route('/search')


# update patient information
@app_views.route('/edit_record/<int:user_id>', methods=["GET", "POST"], strict_slashes=False)
def edit_record(user_id):
    """
        load patient profile to be editted by id
    """ 
    all = db_session.query(Patient)
    # user = db_session.query(Patient).filter(Patient.id == "id").first()
    user = db_session.query(Patient).get(user_id)

    # id = db_session.query(Patient)
    
    form = UpdatePatientForm()
    if form.validate_on_submit():
        user.fname=form.fname.data 
        user.lname=form.lname.data
        user.oname=form.oname.data
        user.address=form.address.data
        user.email=form.email.data
        user.phone=form.phone.data
        user.mob=form.mob.data
        user.yob=form.yob.data
        user.gender=form.gender.data
        user.bloodgroup=form.bloodgroup.data
        user.genotype=form.genotype.data
        user.doctor=form.doctor.data
        user.updated_at=datetime.utcnow()
        db_session.commit()
        flash('Profile edit successful')
        # return redirect(url_for('app_views.index'))
    return render_template('update.html', form=form, user_id=user_id, all=all, user=user)








# delete patient record