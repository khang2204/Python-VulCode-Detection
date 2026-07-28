from flask import Blueprint, request, render_template, send_from_directory
from player_web import get_web
import json
from database_writer import get_db
import constants
import bracket_utils
import requests
import logger
db = None
BASE_URL = 'https://localhost:5000'
endpoints = Blueprint('endpoints', __name__)
LOG = logger.logger(__name__)
@endpoints.route('/')...
if db == None:
init()
tag = request.args.get('tag', default='christmasmike')
data = get_web(db=db)
return render_template('libraries/html/web.html', data=data, tag=tag)
