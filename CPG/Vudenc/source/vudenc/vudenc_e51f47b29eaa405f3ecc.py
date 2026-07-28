import os
from flask import Flask, render_template, request, send_from_directory, redirect, url_for, flash, abort, Response
from flask_login import LoginManager, login_required, login_user, logout_user
from flask_mysqldb import MySQL
from forms import registerForm, loginForm
from passlib.hash import sha256_crypt
from urllib.parse import urlparse, urljoin
from werkzeug.utils import secure_filename
app = Flask(__name__, static_url_path='/static')
UPLOAD_FOLDER = 'C:/Users/s164376/Documents/WebTechTeam/Markis/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['MYSQL_HOST'] = 'cs-students.nl'
app.config['MYSQL_USER'] = 'markis'
app.config['MYSQL_PASSWORD'] = 'dlSvw7noOQbiExlU'
app.config['MYSQL_DB'] = 'markis'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = (
    'kjdnkjfn89dbndh7cg76chb7hjhsbGHmmDDEaQc4By9VH5667HkmFxdxAjhb5Eub')
mysql = MySQL(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'You need to be logged in to view this page!'
@app.route('/')...
conn = mysql.connection
cur = conn.cursor()
cur.execute(
    'SELECT subject_id, subject_name FROM subjects WHERE 1 ORDER BY subject_id ASC'
    )
rv = cur.fetchall()
return render_template('home.html', subjects=rv)
