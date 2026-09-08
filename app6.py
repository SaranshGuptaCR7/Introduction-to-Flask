from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/calculate", methods=["POST"])
def calculate():
    text = request.form.get("text")
    vowels = "aeiouAEIOU"
    count = 0
    for character in text:
        if character in vowels:
            count = count + 1
    return render_template("index.html", result=count, text=text)
if __name__ == "__main__":
    app.run(debug=True)            