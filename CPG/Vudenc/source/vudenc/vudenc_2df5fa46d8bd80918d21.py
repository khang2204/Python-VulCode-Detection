from flask import Flask, render_template, redirect, request
import pg, markdown, time
from time import strftime, localtime
import pg, markdown, time
from wiki_linkify import wiki_linkify
app = Flask('WikiApp')
db = pg.DB(dbname='wiki_db_redo')
@app.route('/')...
return render_template('homepage.html')
