from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
import sqlite3
import jwt
app = Flask(__name__)
api = Api(app)
def get(self):...
query = conn.execute('SELECT * FROM USERS')
i = 0
for row in query:
i = i + 1
return {'Number of users': i}
