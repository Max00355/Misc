from flask import *
from utils.db import db

app = Blueprint(__name__, "developer")

@app.route("/developers/")
def developers():
    return render_template("developers.html")
