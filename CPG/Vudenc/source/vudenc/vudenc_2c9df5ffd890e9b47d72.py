import os
import flask
from werkzeug.wrappers import Response
import psycopg2
from ..config import config
from .. import utils
from ..database import *
from ..initApp import app
from ..auth import check_auth
import ast
addObs = flask.Blueprint('addObs', __name__, static_url_path='/addObs',
    static_folder='static', template_folder='templates')
from flask import make_response, session
from functools import wraps, update_wrapper
from datetime import datetime
def nocache(view):...
@wraps(view)...
response = make_response(view(*args, **kwargs))
response.headers['Last-Modified'] = datetime.now()
response.headers['Cache-Control'
    ] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
response.headers['Pragma'] = 'no-cache'
response.headers['Expires'] = '-1'
return response
