from flask import Flask, flash, render_template, request, url_for, redirect, session, g
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import MySQLdb
from flask_sqlalchemy import SQLAlchemy
from MySQLdb import escape_string as thwart
from passlib.hash import sha256_crypt
import os
import time
from werkzeug import secure_filename
import urllib.request
import shutil
import requests
from datetime import datetime
import sys
time.sleep(30)
app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db:3306/users'
db = SQLAlchemy(app)
os.makedirs('static/videos', exist_ok=True)
__tablename__ = 'User'
UserID = db.Column('UserID', db.Integer, primary_key=True, nullable=False,
    autoincrement=True)
Username = db.Column('Username', db.String(15))
PasswordHash = db.Column('PasswordHash', db.String(200))
DisplayName = db.Column('DisplayName', db.String(15))
def __init__(self, UserID, Username, PasswordHash, DisplayName):...
self.UserID = UserID
self.Username = Username
self.PasswordHash = PasswordHash
self.DisplayName = DisplayName
__tablename__ = 'Video'
VideoID = db.Column('VideoID', db.Integer, primary_key=True, autoincrement=True
    )
UserID = db.Column('UserID', db.Integer, ForeignKey_key='User.UserID',
    nullable=False)
URL = db.Column('URL', db.String(60))
Name = db.Column('Name', db.String(100))
UploadDate = db.Column('UploadDate', db.DateTime)
def __init__(self, VideoID, UserID, URL, Name, UploadDate):...
self.VideoID = VideoID
self.UserID = UserID
self.URL = URL
self.Name = Name
self.UploadDate = UploadDate
secKey = os.urandom(24)
app.secret_key = secKey
limiter = Limiter(app, key_func=get_remote_address)
@app.route('/', methods=['GET', 'POST'])...
error = ''
if request.method == 'POST':
return render_template('index.html', error=error)
return render_template('index.html', error=error)
username = request.form['username']
password = request.form['password']
data = users.query.filter_by(Username=username).first()
if sha256_crypt.verify(password, str(data.PasswordHash)):
session['username'] = username
error = 'Invalid credentials, try again.'
flash('you are now logged in')
return redirect(url_for('upload'))
