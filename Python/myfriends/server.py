from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'TooSecret'
mysql = MySQLConnector(app,'mydb')

@app.route('/')
def index():
    query = "SELECT * FROM allmyfriends"                         
    friends = mysql.query_db(query)                           
    return render_template('index.html', all_friends=friends) 

@app.route('/friends', methods=['POST'])
def create():
    print request.form['name']
    print request.form['age']

    query = "INSERT INTO allmyfriends (name, age, created_at, updated_at) VALUES (:name, :age, NOW(), NOW())"
    data = {
             'name': request.form['name'],
             'age':  request.form['age']
           }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)



app.run(debug=True)
