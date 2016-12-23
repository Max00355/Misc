from flask import *
from routes import *

app = Flask(__name__)

app.register_blueprint(landing.app)
app.register_blueprint(questions.app)
app.register_blueprint(developers.app)

if __name__ == "__main__":
    app.run(debug=True, port=8989)
