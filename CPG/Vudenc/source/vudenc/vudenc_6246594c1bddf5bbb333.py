def post(self):...
post_data = request.get_json(force=True)
user = Table.filter_by(email=post_data.get('email'))
print(e)
if len(user) >= 1 and post_data.get('password'):
response_object = {'status': 'fail', 'message': 'Try again'}
if str(user[0][3]) == str(post_data.get('password')):
response_object = {'status': 'fail', 'message': 'User does not exist.'}
return make_response(jsonify(response_object)), 500
auth_token = encode_auth_token(user[0][0])
response_object = {'status': 'fail', 'message':
    'Password or email do not match.'}
return make_response(jsonify(response_object)), 404
if auth_token:
print(e)
return make_response(jsonify(response_object)), 401
response_object = {'status': 'success', 'id': user[0][0], 'message':
    'Successfully logged in.', 'auth_token': auth_token.decode()}
return {'message': 'Error decoding token'}, 401
return make_response(jsonify(response_object)), 200
