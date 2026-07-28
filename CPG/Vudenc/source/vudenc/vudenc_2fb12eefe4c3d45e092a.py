from flask import Flask, g, jsonify, request
from jsonschema import validate, ValidationError
import argparse
import functools
import sqlite3
"""
[todo] Replace query string concatenations with DB-API’s parameter
substitution to avoid SQL injection attacks.
"""
app = Flask(__name__)
DATABASE_FILE = './tissue.db'
SCHEMA_FILE = './schema.sql'
def validate_request_payload(require_id=False):...
"""docstring"""
def decorator(func):...
@functools.wraps(func)...
request_schema = {'$schema': 'http://json-schema.org/draft-07/schema#',
    'definitions': {'tag': {'type': 'object', 'required': ['namespace',
    'predicate', 'value'], 'properties': {'namespace': {'type': 'string'},
    'predicate': {'type': 'string'}, 'value': {'type': ['number', 'string']
    }}}, 'issue': {'type': 'object', 'required': ['title'], 'properties': {
    'title': {'type': 'string'}, 'description': {'type': 'string'}, 'tags':
    {'type': 'array', 'default': [], 'minItems': 0, 'items': {'$ref':
    '#/definitions/tag'}}}}}}
if require_id:
request_schema['definitions']['issue']['required'].append('id')
request_schema = {**request_schema, **{'type': 'object', 'properties': {
    'data': {'type': 'array', 'minItems': 1, 'items': {'$ref':
    '#/definitions/issue'}}}}}
request_schema['definitions']['issue']['properties']['id'] = {'type': [
    'integer', 'string']}
request_payload = request.get_json()
validate(instance=request_payload, schema=request_schema)
return jsonify({'data': [], 'errors': [
    'failed to validate payload against json schema']}), 400
return func(*args, **kwargs)
