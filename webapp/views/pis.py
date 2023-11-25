
from flask import Flask, render_template, url_for, flash, redirect, request, make_response
from webapp.views import app_views
from models.patient import Patient
from forms import PatientRegForm
from config import db_session


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
@app_views.route('/search')


# update patient information
@app_views.route('/edit-record/<int:id>', methods=["GET", "POST"], strict_slashes=False)
def edit_record(id):
    patient_record = db_session.query(Patient, id)


# delete patient record