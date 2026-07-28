# from Crypto.Cipher import AES
# from Crypto import Random
from flask import Flask,redirect,request, render_template_string, render_template,session,flash,url_for,session,logging,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'Harry Potter And The Deathly Hallows'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

CONFIG = {
    'app_name': 'Damn Vulnerable Flask Application'
}
class User(db.Model):
    """ Create user table """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password
