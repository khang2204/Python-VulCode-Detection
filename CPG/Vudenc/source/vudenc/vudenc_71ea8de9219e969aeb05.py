from flask import Flask, render_template, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_login import LoginManager, current_user, login_user, logout_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import IntegerField, FloatField, DateField, SelectField, SelectMultipleField, FieldList, FormField, StringField, PasswordField, validators
from datetime import datetime
import os.path
import json
import redis
import re
import pprint
pp = pprint.PrettyPrinter(indent=4)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.jinja_env.filters['json_pretty'] = lambda value: json.dumps(value,
    sort_keys=True, indent=4)
Bootstrap(app)
db = redis.Redis('localhost')
user_id = ''
email = ''
password_hash = ''
def get_id(self):...
return self.user_id
