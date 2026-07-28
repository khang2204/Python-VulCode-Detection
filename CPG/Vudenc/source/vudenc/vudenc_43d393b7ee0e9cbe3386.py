import os.path
import re
import motor.motor_tornado
from argon2 import PasswordHasher
from pymongo import MongoClient
import random
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import pymongo
from tornado.options import define, options
define('port', default=8100, help='run on the given port', type=int)
""" BaseHandler():
Class that'll be used later when @tornado.web.authenticated is needed for POST requests.
"""
def get_current_user(self):...
return self.get_secure_cookie('user')
