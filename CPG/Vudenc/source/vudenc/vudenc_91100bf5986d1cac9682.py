from flask import Flask, request, jsonify
import time
import requests
import json
from TextProcessing import makeNGrams
from Ranking import Ranking
import psycopg2
import pprint
import random
random.seed(500)
app = Flask(__name__)
conn_string = (
    "host='green-z.cs.rpi.edu' dbname='index' user='ranking' password='ranking'"
    )
conn = psycopg2.connect(conn_string)
conn.autocommit = True
cursor = conn.cursor()
@app.route('/search', methods=['GET'])...
print('in rec query')
emptyRes = {}
emptyRes['pages'] = []
print(request.args.get('query'))
query = request.args.get('query')
if not query:
return jsonify(emptyRes)
query = query.lower()
rankedList = getRanking(query)
return jsonify(rankedList)
