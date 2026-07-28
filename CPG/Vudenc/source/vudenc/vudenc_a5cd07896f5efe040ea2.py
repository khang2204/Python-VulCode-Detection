from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
app = Flask(__name__)
@app.route('/users')...
mysql = connectToMySQL('users_db')
users = mysql.query_db('SELECT * FROM users;')
return render_template('index.html', users=users)
