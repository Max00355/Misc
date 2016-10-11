from flask import *
import os
import sys

sys.path.append("controller_backend")

app = Flask(__name__, template_folder="controller_frontend")

for x in os.listdir("controller_backend"):
    if x.endswith(".py"):
        app.register_blueprint(__import__(x.split(".")[0]).controller)
        
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
