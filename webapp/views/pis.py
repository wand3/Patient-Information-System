
from flask import Flask, render_template, url_for, flash, redirect, request, make_response
from webapp.views import app_views
from models.patient import Patient
from forms import PatientRegForm, UpdatePatientForm
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
                        bloodGroup=form.bloodGroup.data,
                        genotype=form.genotype.data,
                        history=form.history.data,
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
    user = db_session.query(Patient).filter(Patient.id == "id").first()
    # id = db_session.query(Patient)
    
    form = UpdatePatientForm(obj=user)
    if form.validate_on_submit():
        # new_edit = form.populate_obj(id)
        # new_edit = db_session.query(Patient).filter(Patient.id == "id").update(dict(
        #         fname=form.fname.data, 
        #         lname=form.lname.data,
        #         oname=form.oname.data,
        #         address=form.address.data,
        #         email=id.email,
        #         phone=form.phone.data,
        #         mob=form.mob.data,
        #         yob=form.yob.data,
        #         gender=form.gender.data,
        #         bloodGroup=form.bloodGroup.data,
        #         genotype=form.genotype.data,
        #         history=form.history.data,
        #         doctor=form.doctor.data,), synchronize_session="fetch"
        #     )
        new_edit = Patient(
                fname=form.fname.data, 
                lname=form.lname.data,
                oname=form.oname.data,
                address=form.address.data,
                email=form.email.data,
                phone=form.phone.data,
                mob=form.mob.data,
                yob=form.yob.data,
                gender=form.gender.data,
                bloodGroup=form.bloodGroup.data,
                genotype=form.genotype.data,
                history=form.history.data,
                doctor=form.doctor.data,
                updated_at=datetime.utcnow()
            )
        db_session.add(new_edit)
        db_session.commit()
        flash('Profile edit successful')
        return redirect(url_for('app_views.index'))
    return render_template('update.html', form=form, user_id=user_id, all=all)








# delete patient record