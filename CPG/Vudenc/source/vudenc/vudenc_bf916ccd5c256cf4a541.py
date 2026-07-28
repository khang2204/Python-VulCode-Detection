from flask import request
from flask_jwt_extended import jwt_required
from flask_restplus import Namespace, Resource, fields
from utilities import database_utilities
api = Namespace('users', description='Information relating to users')
def get(self):...
"""docstring"""
return database_utilities.execute_query('select * from users')
