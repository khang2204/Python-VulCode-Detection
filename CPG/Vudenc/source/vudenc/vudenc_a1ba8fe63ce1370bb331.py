import sys
import ConfigParser as cp
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from flaskext.mysql import MySQL
from MeetingScheduler import register as reg
from MeetingScheduler import user as usr
from MeetingScheduler import calendar
configPath = './config/mysql.config'
if len(sys.argv) == 2:
configPath = sys.argv[1]
parser = cp.ConfigParser()
parser.read(configPath)
user = parser.get('MySQLConfig', 'user')
password = parser.get('MySQLConfig', 'password')
db = parser.get('MySQLConfig', 'database')
host = parser.get('MySQLConfig', 'host')
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = user
app.config['MYSQL_DATABASE_PASSWORD'] = password
app.config['MYSQL_DATABASE_DB'] = db
app.config['MYSQL_DATABASE_HOST'] = host
mysql.init_app(app)
app.secret_key = 'FKWNDJS(23/sd32!jfwedn/f,?REsdjtwed'
def isUserAuthorized():...
username, password = getUsernameAndPassword()
response = usr.validateCredentials(username, password, mysql)
return response
