from flask import render_template, request, redirect, url_for

from . import app

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/projects", methods=["GET"])
def projects():
    return render_template("projects.html")




