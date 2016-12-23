from flask import *
from utils.db import db

app = Blueprint(__name__, "questions")

@app.route("/question/1")
def question1():
    return render_template("question1.html")

@app.route("/question/2")
def question2():
    return render_template("question2.html")

@app.route("/question/3")
def question3():
    return render_template("question3.html")

@app.route("/question/4")
def question4():
    return render_template("question4.html")

@app.route("/question/", methods=['POST'])
def postQuestion():
    return "ASD"
