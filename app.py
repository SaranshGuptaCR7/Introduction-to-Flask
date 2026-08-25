from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html") 
@app.route("/calculate", methods=["POST"])
def calculate():
    units = int(request.form["units"])
    bill = units * 5
    if units <= 100:
        message = "Good Boy! Energy Saver"
    elif units <=200:
        message = "Decent! Son Work Hard!"
    else:
        message = "Damn!Looks like bro like Elon Musk then buy me a BMW M4 Competition Edition, around 15 billion dollars too and some billion dollars property"
    return render_template("index.html", units=units, bill=bill, message=message)
if __name__ == "__main__":
    app.run(debug=True)      