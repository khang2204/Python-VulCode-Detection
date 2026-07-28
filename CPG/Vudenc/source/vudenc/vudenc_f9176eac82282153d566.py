from flask import Flask, render_template, jsonify, request, make_response, session, abort
from flask.ext.sqlalchemy import SQLAlchemy
from flask_mail import Message, Mail
from flask_login import LoginManager
from re import compile
import random, string
from base64 import *
from beaker.middleware import SessionMiddleware
from models import User, db
from bananas import bananas
app = Flask(__name__)
session_opts = {'session.type': 'file', 'session.cookie_expires': 1800,
    'session.data_dir': '/tmp/cache/data', 'session.lock_dir':
    '/tmp/cache/data', 'session.auto': False}
app.wsgi_app = SessionMiddleware(app.wsgi_app, session_opts)
import gamechange.error
app.config.from_envvar('FLASK_CONFIG')
db.init_app(app)
mail = Mail(app)
app.register_blueprint(bananas, url_prefix='/bananas', config=app.config)
@app.route('/initDB')...
db.create_all()
return 'This is naughty and MUST not be in production!'
