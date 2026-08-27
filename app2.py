from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/calculate", methods=["POST"])
def calculate():
    water_consumed = int(request.form["consumed"])
    daily_water = int(request.form["goal"])
    name = request.form["name"]
    percentage = (water_consumed / daily_water) *100
    if water_consumed >= daily_water:
        message = "Good boy!Son you doing good"
    else:
        message = "Son! Drink water otherwise you will becam the first human being to become a twick"
    return render_template("index.html", percentage=percentage, message=message)
if __name__ == "__main__":
    app.run(debug=True)       