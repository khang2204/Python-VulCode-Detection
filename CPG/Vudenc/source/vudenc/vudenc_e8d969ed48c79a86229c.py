from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from ...models import Table
from ....utils import jwt_required
comments_blueprint = Blueprint('comments', __name__)
""" Update Instance api resource """
@jwt_required...
post_data = request.get_json(force=True)
response = Table.save(answer_id, data=post_data)
if response:
response_object = {'status': 'success', 'message':
    'Your comment was successful'}
response_object = {'status': 'fail', 'message':
    'Some error occurred. Please try again.'}
return make_response(jsonify(response_object)), 201
return make_response(jsonify(response_object)), 400
