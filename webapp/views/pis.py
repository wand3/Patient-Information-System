
from flask import Flask, render_template, url_for
from webapp.views import app_views


# add patient route
@app_views.route('/', methods=['GET'], strict_slashes=False)
def index():
    return render_template("index.html")


# get patient route


# update patient information