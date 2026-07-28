__author__ = 'Kyle Chesney'
from flask import *
from flask_login import LoginManager
import sqlite3
from datetime import datetime as dt
app = Flask(__name__)
login = LoginManager(app)
@app.route('/')...
return render_template('login.html')
