from flask import *
from pymongo import MongoClient
import uuid
import time

db = MongoClient("localhost", 27017).speakyourmind
app = Flask(__name__)
app.secret_key = "1939ds9sdlfll324l234;s;dfllkkasdkasdl213l12o931299asdjncnzxnkaskdhaHKjhdsKskjhdIOQWUEOIDU*fhfHDSF"

@app.route("/", methods=['GET'])
def getSnips():
    if "id" not in session:
        session['id'] = uuid.uuid4().hex
    return render_template("index.html")

@app.route("/", methods=['POST'])
def postSnip():
    if "id" not in session:
        return redirect("/")
    snip = request.data['snip'][:255]
    check = db.snips.find_one({
        "poster":session['id'],
        "created_at":{"$lt":time.time() - 60 * 10}
    })
    if check:
        return "You can't post more than once every 10 minutes"
    db.snips.insert({
        "poster":session['id'],
        "snip":snip,
        "likes":[],
        "created_at":time.time()
    })
    return "Snip Posted!"

@app.route("/snips", methods=['GET'])
def getSnipsJson():
    snips = db.snips.find().sort("_id", -1).limit(100)
    return jsonify(list(snips))

if __name__ == "__main__":
    app.run(debug=True, port=1337)
