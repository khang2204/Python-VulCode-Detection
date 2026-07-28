import subprocess
import shlex
import os
import signal
from helper import path_dict, path_number_of_files, pdf_stats, pdf_date_format_to_datetime
import json
from functools import wraps
from urllib.parse import urlparse
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
import time
app = Flask(__name__)
app.secret_key = 'Aj"$7PE#>3AC6W]`STXYLz*[G\\gQWA'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mountain'
app.config['MYSQL_DB'] = 'bar'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
WGET_DATA_PATH = 'data'
PDF_TO_PROCESS = 10
MAX_CRAWLING_DURATION = 60
WAIT_AFTER_CRAWLING = 1000
def is_logged_in(f):...
@wraps(f)...
if 'logged_in' in session:
return f(*args, **kwargs)
flash('Unauthorized, Please login', 'danger')
return redirect(url_for('login'))
