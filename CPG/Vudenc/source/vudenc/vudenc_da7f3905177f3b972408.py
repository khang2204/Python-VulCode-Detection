import os
import time
import logging
from flask import jsonify
from flask import Flask, request
from flask import render_template
from flask import send_from_directory
import Importer
from DataSource.MySQLDataSource import MySQL
import Config
from Config import logger
app = Flask(__name__)
LOG_DIR = os.environ['LOGFILES_PATH'
    ] if 'LOGFILES_PATH' in os.environ else './logs/'
UPLOADS_DIR = os.environ['DATAFILES_PATH'
    ] if 'DATAFILES_PATH' in os.environ else './uploads/'
DATABASE = os.environ['DB_NAME'] if 'DB_NAME' in os.environ else 'astronomy'
@app.route('/')...
return explore()
