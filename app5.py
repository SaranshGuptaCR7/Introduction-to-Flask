from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/calculate", methods=["POST"])
def calculate():
    height = int(request.form.get("height"))
    weight = int(request.form.get("weight"))
    name = request.form.get("name")
    bmi = weight / height ** 2
    if bmi >= 18.5:
        msg = "Son! U r doing good"
    else:
        msg = "Son! u hurry and get some fatty or height"
    return render_template("index.html", bmi=bmi, msg=msg, name=name)    
if __name__ == "__main__":
    app.run(debug=True)