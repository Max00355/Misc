from flask import *
import requests
import StringIO

app = Flask(__name__)

@app.route("/")
def serve_page():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def email_stuff():
    your_name = request.form['your-name']
    your_email = request.form['your-email']
    team_name = request.form['team-name']
    roster_info = request.form['roster-info']
    print requests.post("https://api.mailgun.net/v3/sandbox0f6f729dc00e48668fae776b1eb0b834.mailgun.org/messages",
            auth=("api", "key-59745b378f6aa7b0273707b72cceb3bc"),
            files={
                "attachment[0]": (team_name + ".txt", StringIO.StringIO(roster_info))
            },
            data= {
                "from":"Roster Submission <postmaster@sandbox0f6f729dc00e48668fae776b1eb0b834.mailgun.org>",
                "to":["max00355@gmail.com"],
                "cc":["frankieprimerano@gmail.com"],
                "subject":team_name,
                "text":"""Dear {},

Thank you for submitting your roster information!
                """.format(your_name),
            }).content
    return "Okay"
if __name__ == "__main__":
    app.run(debug=True)

