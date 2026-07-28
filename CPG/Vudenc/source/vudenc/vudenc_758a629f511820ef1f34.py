from flask import Flask, request
from db import Database
from datetime import datetime, timedelta
from log import Logger
import sql_queries
import simplejson
logger = Logger().logger
app = Flask(__name__)
port_number = 40327
database = Database()
cuisine_discovery_cache = {}
unique_ingredients_cache = {}
cache_persistence_time = timedelta(days=1)
geodist = 0.12
@app.before_request...
return
