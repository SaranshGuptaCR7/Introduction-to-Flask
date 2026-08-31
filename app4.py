from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")
@app.route("/calculate", methods=["POST"])
def calculate():
    date1 = request.form.get("date1")
    date2 = request.form.get("date2")

    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")

    difference = date2 - date1
    days = difference.days
    return render_template("index.html", days=days)
if __name__ == "__main__":
    app.run(debug=True)