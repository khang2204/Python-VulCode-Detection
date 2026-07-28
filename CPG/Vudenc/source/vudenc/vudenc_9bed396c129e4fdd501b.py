from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from ...models import Table
from ....utils import jwt_required
answers_blueprint = Blueprint('answers', __name__)
""" Update Instance api resource """
@jwt_required...
data = request.get_json(force=True)
response = Table.update(question_id, answer_id, data)
if response == 200:
response_object = {'status': 'success', 'message': 'Update successful'}
if response == 302:
return make_response(jsonify(response_object)), 200
response_object = {'status': 'fail', 'message':
    'Please provide correct answer and question id'}
if response == 203:
return make_response(jsonify(response_object)), 400
response_object = {'status': 'fail', 'message': 'Unauthorized request.'}
response_object = {'status': 'fail', 'message':
    'Please provide correct answer and question id'}
return make_response(jsonify(response_object)), 401
return make_response(jsonify(response_object)), 400
