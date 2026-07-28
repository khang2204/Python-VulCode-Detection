from flask import Flask, render_template, request, jsonify, redirect
from flask_assets import Bundle, Environment
from flask_login import LoginManager
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime
import sqlite3
import re
import json
import libgravatar
import sys
import asyncio
import LocalSettings
app = Flask(__name__)
FLASK_PORT_SET = int(sys.argv[1])
FLASK_PORT_SET = LocalSettings.FLASK_HOST_PORT
conn = sqlite3.connect(LocalSettings.SQLITE3_FILENAME, check_same_thread=False)
print(' * 강제 포트 설정 지정됨.')
curs = conn.cursor()
curs.execute('select * from FORM_DATA_TB limit 1')
DATABASE_QUERY = open('tables/initial.sql').read()
CONVERSTATIONS_NATIVE = open('dic.json', encoding='utf-8').read()
curs.executescript(DATABASE_QUERY)
CONVERSTATIONS_DICT = json.loads(CONVERSTATIONS_NATIVE)
conn.commit
bundles = {'main_js': Bundle('js/bootstrap.min.js', output='gen/main.js'),
    'main_css': Bundle('css/minty.css', 'css/custom.css', output=
    'gen/main.css')}
assets = Environment(app)
assets.register(bundles)
@app.route('/', methods=['GET', 'POST'])...
BODY_CONTENT = ''
BODY_CONTENT += open('templates/index_content.html', encoding='utf-8').read()
BODY_CONTENT = BODY_CONTENT.replace('| version |', LocalSettings.OFORM_RELEASE)
curs.execute('select * from FORM_DATA_TB')
form_data = curs.fetchall()
for i in range(len(form_data)):
return render_template('index.html', OFORM_APPNAME=LocalSettings.
    OFORM_APPNAME, OFORM_CONTENT=BODY_CONTENT)
