from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from wtforms import Form, BooleanField, StringField, PasswordField, validators
import re
import md5
import os, binascii


salt = binascii.b2a_hex(os.urandom(15))
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
app = Flask(__name__)
app.secret_key = 'thissecret'
mysql = MySQLConnector(app, 'thewall') #change mydb to the name of my model that I will create



def check_email(email):
    reexp = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
    checked_email = reexp.match(email)
    print checked_email
    return checked_email

@app.route('/')
def index():

        return render_template('index.html')

@app.route('/wall')
def wall():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template("wall.html", all_users=users)


@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    rpassword = request.form['password']
    password = request.form['password']
    salt =  binascii.b2a_hex(os.urandom(15))
    hashed_pw = md5.new(password + salt).hexdigest()

    # if (first_name).isalpha():
    #     if len(first_name)<1:
    #         flash("first Name cannot be empty!")

    # elif(last_name).isalpha():
    #     if len(last_name) < 1:
    #         flash("last name cannot be empty ")
    
    # elif len(email) > 0:
    #     if(check_email(email) == None):
    #         flash("Not a right email !!!")
    #     else:
    #         flash("right email")

    # elif len(passworld)>=8 and len(rpassword)>=8:
    #     if(passworld != rpassword):
    #         flash("incorrect password")
    query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :hashed_pw, NOW(), NOW())"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email': request.form['email'],
             'hashed_pw':hashed_pw

           }
    mysql.query_db(query, data)
    # return render_template("wall.html")

    # else:

    #     flash("You are now registered!!")
    return redirect("/wall") 

    


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    query = "SELECT users.id, users.password FROM users WHERE users.email = :email"
    print query
    data = {
        'email': email,
        'password': password
    }


    see = mysql.query_db(query, data)
    print see 
    return render_template('wall.html')



app.run(debug=True)
