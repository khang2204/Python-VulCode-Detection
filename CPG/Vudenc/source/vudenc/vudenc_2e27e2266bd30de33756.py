def post(self):...
post_data = request.get_json(force=True)
user = Table.filter_by(post_data.get('email'))
if not user:
response_object = {'status': 'fail', 'message':
    'User already exists. Please Log in.'}
user = Table.save(data=post_data)
print(e)
return make_response(jsonify(response_object)), 202
auth_token = encode_auth_token(user.get('id')).decode()
response_object = {'status': 'fail', 'message':
    'Some error occurred. Please try again.'}
response_object = {'status': 'success', 'message':
    'Successfully registered.', 'id': user.get('id'), 'auth_token': auth_token}
return make_response(jsonify(response_object)), 401
return make_response(jsonify(response_object)), 201
