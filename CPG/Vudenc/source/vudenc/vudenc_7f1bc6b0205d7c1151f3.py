from operator import itemgetter
import psycopg2
from psycopg2.extras import DictCursor
from flask import Flask
from flask import render_template
from flask import request
from gensim.models import Doc2Vec
import re
import argparse
application = Flask(__name__)
"""Helpers"""
def get_subjects():...
cur = conn.cursor()
query = 'SELECT subject, count(*) FROM articles group by subject;'
cur.execute(query)
subjects = sorted(cur.fetchall(), key=lambda tup: tup[0])
return subjects
