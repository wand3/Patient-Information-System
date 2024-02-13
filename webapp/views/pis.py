
from flask import Flask, render_template, url_for, flash, redirect, request, make_response
from webapp.views import app_views
from sqlalchemy import or_
from models.patient import Patient
from forms import PatientRegForm, UpdatePatientForm
# from sqlalchemy import update
from config import db_session
from flask_login import current_user, login_required
from datetime import datetime
from webapp.auth import has_role


@app_views.route('/', methods=['GET'], strict_slashes=False)
def index():
    return render_template("index.html")


# Patient profile route
@login_required
@app_views.route('/patient/<int:id>', methods=["GET"], strict_slashes=False)
@has_role('administrator', 'record_officer')
def patient_profile(id):
        
    all = db_session.query(Patient)
    user = db_session.query(Patient).get(id)
    if user not in all:
        flash("Patient has no record consider registering")
        # return redirect(url_for("app_views.index"))
    return render_template("patient_profile.html", user=user)


# Delete patient record route
@login_required
@app_views.route('/delete/<int:id>', methods=['GET', 'POST'], strict_slashes=False)
@has_role('administrator', 'record_officer')
def delete_record(id):
    user = db_session.query(Patient).get(id)
    db_session.delete(user)
    db_session.commit()
    flash("Patient record succesfully deleted")
    return redirect(url_for("app_views.index", id=user.id))


# Patient Registeration route
@login_required
@app_views.route('/register', methods=['GET', 'POST'], strict_slashes=False)
@has_role('administrator', 'record_officer')
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
                        dob=form.dob.data,
                        gender=form.gender.data,
                        bloodgroup=form.bloodgroup.data,
                        genotype=form.genotype.data,
                        marital_status=form.marital_status.data,
                        )
        db_session.add(new_patient)
        db_session.commit()
        db_session.close()
        flash('Thanks for registering')
        return redirect(url_for('app_views.index'))
    return render_template("register.html", form=form)

# search patient
@login_required
@app_views.route('/search', methods=["GET"], strict_slashes=False)
def search():
    resp = request.args.get("search_object")
    print(resp)
    if resp:
        results = db_session.query(Patient).filter(or_(Patient.email.ilike(f'%{resp}%')), Patient.id.ilike(f'%{resp}%')).order_by(Patient.id.desc()).all()
        # results = db_session.query(Patient).filter(Patient.id.ilike(f'%{resp}%')).order_by(Patient.id.desc()).all()

    else:
        results = ["fack"]

    return render_template("search_patient.html", results=results)


# update patient information
@login_required
@app_views.route('/edit_record/<int:user_id>', methods=["GET", "POST"], strict_slashes=False)
@has_role('administrator', 'record_officer')
def edit_record(user_id):
    """
        load patient profile to be editted by id
    """ 
    all = db_session.query(Patient)
    user = db_session.query(Patient).get(user_id)
    form = UpdatePatientForm()

    # default_genotype = user.genotype
    form.genotype.default = user.genotype
    form.dob.default = user.dob
    form.gender.default = user.gender
    form.bloodgroup.default = user.bloodgroup
    form.email.default = user.email
    form.oname.default = user.oname
    form.phone.default = user.phone
    # form.process()
    # form.process(default_genotype)

    if form.validate_on_submit():
        user.fname=form.fname.data 
        user.lname=form.lname.data
        user.oname=form.oname.data
        user.address=form.address.data
        user.email=form.email.data
        user.phone=form.phone.data
        user.dob=form.dob.data
        user.gender=form.gender.data
        user.bloodgroup=form.bloodgroup.data
        user.genotype=form.genotype.data
        user.marital_status=form.marital_status.data
        user.updated_at=datetime.utcnow()
        db_session.commit()
        flash('Profile edit successful')
        return redirect(url_for('app_views.patient_profile', id=user.id))
    return render_template('update.html', form=form, user_id=user_id, all=all, user=user)


# delete patient record
