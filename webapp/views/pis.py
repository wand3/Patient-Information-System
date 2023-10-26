
from flask import Flask, render_template, url_for
from webapp.views import app_views
from forms import PatientRegForm


# index route
@app_views.route('/', methods=['GET'], strict_slashes=False)
def index():
    return render_template("register.html")

# Patient Registeration route
@app_views.route('/register', methods=['POST'], strict_slashes=False)
def register():
    form = PatientRegForm
    def pre_validate(self, form):
        """
        Override if you need field-level validation. Runs before any other
        validators.

        :param form: The form the field belongs to.
        """
        pass
    return render_template("register.html", form=form)

# get patient route


# update patient information
