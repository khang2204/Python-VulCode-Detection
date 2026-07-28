from flask import jsonify, Response, send_from_directory, request
from api_decorators import *
from api_utils import *
from models import Server, Sequence, SequenceItem, NotFoundError, Property, Device, INDIProfile, ImagesDatabase, camera_images_db, main_images_db, commands
import os
from controller import controller
from app import app
import logging
import io
default_settings = {}
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
is_debug_mode = int(os.environ.get('DEV_MODE', '0')) == 1
app.logger.setLevel(os.environ.get('LOG_LEVEL', 'DEBUG' if is_debug_mode else
    'INFO'))
@app.route('/api/version')...
return app.config['version']
