from flask import Flask, g, render_template, request, jsonify
from utils import get_db, get_queries, shutdown, ajax, execute_query, generic_search
import os
import atexit
app = Flask(__name__)
atexit.register(shutdown, app=app, context=g)
app.config.update({'DB_USER': os.environ['IDBS_USER'], 'DB_PWD': os.environ
    ['IDBS_PWD'], 'DB_SERVER': 'diassrv2.epfl.ch', 'DB_PORT': 1521,
    'DB_SID': 'orcldias', 'DEBUG': True, 'QUERIES_PATH': 'queries.sql'})
@app.route('/')...
con = get_db(app, g)
return render_template('index.html')
