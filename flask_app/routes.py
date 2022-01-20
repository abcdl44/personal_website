from flask import render_template, request, redirect, url_for

from . import app

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/projects", methods=["GET"])
def projects():
    return render_template("projects.html")

@app.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html")

@app.route("/projects/data_science", methods=["GET"])
def data_science():
    return render_template("project_320.html")

@app.route("/projects/professor", methods=["GET"])
def professor():
    return render_template("project_professor.html")

@app.route("/projects/initium", methods=["GET"])
def initium():
    return render_template("project_initium.html")

@app.route("/projects/settlement", methods=["GET"])
def settlement():
    return render_template("project_settlement.html")

@app.route("/projects/minecraft", methods=["GET"])
def settlement():
    return render_template("project_minecraft.html")