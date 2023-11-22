
from flask import Flask, render_template, url_for, flash, redirect, request, make_response
from webapp.views import app_views
from forms import PatientRegForm
from models import Patient
from config import Config
from sqlalchemy.orm import Session

# index route
@app_views.route('/', methods=['GET'], strict_slashes=False)
def index():
    return render_template("index.html")


# Patient Registeration route
@app_views.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    form = PatientRegForm()
    # db_session = Config.Session
    # resp = make_response(render_template('register.html', form=form))
    # request.headers['Content-Type'] = 'application/json'
    
    if request.method == 'POST' and form.validate():
        """
            Override if you need field-level validation. Runs before any other
            validators.

            :param form: The form the field belongs to.
        """
    # new_patient = request.get_json()
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
        Session.add(new_patient)
        Session.commit()
        flash('Thanks for registering')
        return redirect(url_for('index'))
    return render_template("register.html", form=form)
    # return resp

# get patient route


# update patient information


