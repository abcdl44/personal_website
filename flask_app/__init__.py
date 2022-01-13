from flask import Flask, render_template, request, redirect, url_for

import os

def page_not_found(e):
    return render_template("404.html"), 404

app = Flask(__name__)

app.register_error_handler(404, page_not_found)

from . import routes