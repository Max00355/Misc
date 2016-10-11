from flask import *
import pykeyboard

controller = Blueprint(__name__, "snes")
keyboard = pykeyboard.PyKeyboard()

@controller.route("/snes/", methods=['GET'])
def controller_template():
    return render_template("snes.html")

@controller.route("/snes/", methods=['POST'])
def control():
    allowed_keys = [
        "a",
        "b",
        "x",
        "y", 
        "r", # RB
        "l", # LB
        "t", # Up
        "f", # Left
        "g", # Down
        "h" # Right
    ]

    data = request.form
    if "keydown" in data:
        if data['keydown'] in allowed_keys:
            keyboard.press_key(data['keydown'])
    elif "keyup" in data:
        if data['keyup'] in allowed_keys:
            keyboard.release_key(data['keyup'])
    return "OKAY"


