
from flask import Flask, render_template, url_for, flash, redirect, request
from webapp.views import app_views
from forms import PatientRegForm
from models import Patient
from config import Config


# index route
@app_views.route('/', methods=['GET'], strict_slashes=False)
def index():
    return render_template("index.html")


# Patient Registeration route
@app_views.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    form = PatientRegForm()
    db_session = Config
    if request.method == 'POST' and form.validate():
        """
        Override if you need field-level validation. Runs before any other
        validators.

        :param form: The form the field belongs to.
        """
        new_patient = Patient( form.fname.data, 
                          form.lname.data,
                          form.oname.data,
                          form.address.data,
                          form.email.data,
                          form.phone.data,
                          form.mob.data,
                          form.yob.data,
                          form.gender.data,
                          form.bloodGroup.data,
                          form.genotype.data,
                          form.history.data,
                          form.doctor.data,
                          )
        db_session.new(new_patient, form)
        db_session.save()
        flash('Thanks for registering')
        return redirect(url_for('index'))
    return render_template("register.html", form=form)

# get patient route


# update patient information
