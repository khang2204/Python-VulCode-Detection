from flask import Flask
from flask_restful import Api, Resource, reqparse
from WebHandler import getHTML
app = Flask(__name__)
api = Api(app)
def get(self, name):...
return getHTML(name)
