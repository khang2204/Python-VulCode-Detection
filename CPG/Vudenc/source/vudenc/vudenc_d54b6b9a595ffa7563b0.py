from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy, sqlalchemy
from flask.ext.socketio import emit, SocketIO
import os, uuid, psycopg2
app = Flask(__name__, template_folder='pages')
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'
    ] = 'postgresql://ubuntu:Unl0ck@localhost/unlock'
app.config['SECRET_KEY'] = 'something unique and secret'
db = SQLAlchemy(app)
socketIO = SocketIO(app)
url_prefix = 'https://capstone-brocksmith225.c9users.io/'
__tablename__ = 'unlock_users'
email = db.Column(db.String(40), unique=True, primary_key=True)
pwd = db.Column(db.String(64))
progress = db.Column(db.Integer, default=1)
level1_progress = db.Column(db.Integer, default=0)
level2_progress = db.Column(db.Integer, default=0)
level3_progress = db.Column(db.Integer, default=0)
level4_progress = db.Column(db.Integer, default=0)
authenticated = db.Column(db.Boolean, default=False)
difficulty = db.Column(db.Integer, default=0)
def is_active(self):...
return True
