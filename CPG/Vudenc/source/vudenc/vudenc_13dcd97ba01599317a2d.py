from flask import Flask, url_for, render_template, request, make_response, jsonify, json, Response
import requests
from requests_oauthlib import OAuth1
from knowyourgov import app
from knowyourgov.models import Politician
from knowyourgov.scripts import insert_politicians_in_db
from knowyourgov.scripts.scraping import scrapers
"""Home page
"""
@app.route('/')...
q = Politician.all()
q.order('-search_count')
politicians = []
count = 0
for politician in q:
politicians.append(politician)
return render_template('home.html', politicians=politicians)
count = count + 1
if count == 8:
