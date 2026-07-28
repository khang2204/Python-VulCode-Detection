from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, static_folder='static', static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.sqlite3'
app.config['SECRET_KEY'] = 'random string'
db = SQLAlchemy(app)
id = db.Column(db.Integer, primary_key=True)
email = db.Column(db.String(50))
password = db.Column(db.String(20))
def __init__(self, email, password):...
self.email = email
self.password = password
@app.route('/')...
return render_template('home.html')
