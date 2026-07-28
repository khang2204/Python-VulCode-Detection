"""
Flask App for Todo List MVP
"""
from flask import abort, Flask, jsonify
from flask import render_template, request, url_for
import json
from models import storage, Task, User, REQUIRED, PORT, HOST
import requests
from uuid import uuid4
app = Flask(__name__)
app.url_map.strict_slashes = False
ERRORS = ['Not a JSON', 'Missing required information', 'Missing id',
    'Wrong id type']
def api_response(state, message, code):...
"""docstring"""
response = {state: message, 'status_code': code}
resp_json = jsonify(message)
return resp_json
