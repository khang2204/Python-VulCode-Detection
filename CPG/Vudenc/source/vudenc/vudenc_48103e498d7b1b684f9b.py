from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask.ext.sqlalchemy import SQLAlchemy
from oauth import OAuthSignIn
from subprocess import check_output, STDOUT, CalledProcessError
from werkzeug import generate_password_hash, check_password_hash, secure_filename
from database.database_create import Base, User
from database.database_insert import insert_user, insert_social_user
from database.database_query import query_user, query_social_user, number_of_users
import base64
import json
import os
import shutil
import tempfile
import parser
DEBUG = True
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['OAUTH_CREDENTIALS'] = {'facebook': {'id': '604820106335654',
    'secret': '5eb3f15f84c722df9cbc577206557cc8'}, 'twitter': {'id':
    'cGFr2WV93py7an7FrGXXNDS6p', 'secret':
    'U9ufkrhicVHrj5CGojmQ7ZCxSwytoShSgM0t9WCq0HbqcfKwL8'}}
app.secret_key = 'fe2917b485cc985c47071f3e38273348'
app.config['UPLOAD_FOLDER'] = 'userFiles/'
app.config['ALLOWED_EXTENSIONS'] = set(['pml'])
def get_resource_as_string(name, charset='utf-8'):...
return f.read().decode(charset)
