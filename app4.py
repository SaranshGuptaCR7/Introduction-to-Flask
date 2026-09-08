from flask import Flask, render_template, request
import mysql.connector
import re
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def login():
    msg = '' 
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="52341",
            database="flask_login"
        )
        mycursor = mydb.cursor()
        mycursor.execute(
            "SELECT * FROM LoginDetails WHERE NAME=%s AND PASSWORD=%s",
            (username, password)
        )
        account = mycursor.fetchone()
        if account:
            name = account[1]
            id = account[0]
            msg = 'Logged in Successfully'
            return render_template('welcome.html', msg=msg, name=name, id=id)
        else:
            msg = 'Incorrect Credentials'
    return render_template('login.html', msg=msg)
@app.route('/logout')
def logout():
    name = ''
    id = ''
    msg = "Logged out successfully Son! So U better do no show your face again!"
    return render_template('login.html', msg=msg, name=name, id=id)
@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root", 
            password = "52341",
            database = "flask_login"
        )
        mycursor = mydb.cursor()
        mycursor.execute(
            "SELECT * FROM LoginDetails WHERE Name=%s OR Email_id=%s",
            (username, email)
        )
        account = mycursor.fetchone()
        if account:
            msg = "Account already exists! SON What U Doing?"
        elif not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
            msg = "Username must be letter/numbers only!"
        else:
            mycursor.execute(
                "INSERT INTO LoginDetails (Name, Password, Email_id) VALUES (%s, %s, %s)",
            )  
            mydb.commit()
            msg = "Registration successfull"
            return render_template('login.html', msg=msg)
    return render_template('register.html', msg=msg)
if __name__ == "__main__":
    app.run(debug=True)          