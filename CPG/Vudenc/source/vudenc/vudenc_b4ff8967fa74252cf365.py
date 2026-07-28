from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from ...models import Table
from ....utils import jwt_required, encode_auth_token
auth_blueprint = Blueprint('auth', __name__)
"""
    User Signup API Resource
    """
def post(self):...
post_data = request.get_json(force=True)
user = Table.filter_by(post_data.get('email'))
if not user:
response_object = {'status': 'fail', 'message':
    'User already exists. Please Log in.'}
user = Table.save(data=post_data)
print(e)
def delete(self, user_id=None):...
return make_response(jsonify(response_object)), 202
auth_token = encode_auth_token(user.get('id')).decode()
response_object = {'status': 'fail', 'message':
    'Some error occurred. Please try again.'}
post_data = request.get_json(force=True)
response_object = {'status': 'success', 'message':
    'Successfully registered.', 'id': user.get('id'), 'auth_token': auth_token}
return make_response(jsonify(response_object)), 401
Table.delete(user_id, post_data)
return make_response(jsonify(response_object)), 201
response_object = {'status': 'success', 'message': 'User deleted successfully.'
    }
return make_response(jsonify(response_object)), 200
