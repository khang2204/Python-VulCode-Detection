from flask import Blueprint, request
from api import require_apikey
from api.apiutils import *
locations = Blueprint('location', __name__)
@locations.route('/ping')...
return 'pong'
