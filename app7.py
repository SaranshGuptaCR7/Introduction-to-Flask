from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("register.html")
@app.route("/register", methods=["POST", "GET"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    email = request.form.get("e-mail")
    achievements = request.form.get("achievments")
    print("Username:", username)
    print("Password:", password)
    print("E-mail", email)
    print("Achievements:", achievements)
    return "Registeration completled Son!"
if __name__ == "__main__":
    app.run(debug=True)