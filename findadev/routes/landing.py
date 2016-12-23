from flask import *

app = Blueprint(__name__, "landing")

@app.route("/")
def landing():
    return render_template("index.html")
