from flask import request
from flask_jwt_extended import jwt_required
from flask_restplus import Namespace, Resource, fields, reqparse
from utilities import database_utilities
api = Namespace('spaces', description='Information relating to spaces')
def get(self):...
"""docstring"""
parser = reqparse.RequestParser()
parser.add_argument('building_id')
args = parser.parse_args()
where_query = 'WHERE building_id = %s' if args['building_id'] else ''
query = f'SELECT * FROM spaces {where_query}'
parameters = args['building_id'],
return database_utilities.execute_query(query, parameters)
