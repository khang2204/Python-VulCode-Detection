import os
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
import psycopg2
import timeit
from fieldValues import faculty_status, fields_of_study, departments, careerareas, ipedssectornames
from occupations import occupations
project_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_url_path='', static_folder='static')
query1 = (
    'SELECT year,faculty, count(*) as N from hej where faculty=1 group by faculty,year;'
    )
@app.route('/', methods=['GET'])...
return render_template('home.html')
