@jwt_required...
if user_id:
user = Table.filter_by(email=None, user_id=user_id)
response_object = {'results': Table.query(), 'status': 'success'}
if len(user) < 1:
return jsonify(response_object), 200
response_object = {'results': 'User not found', 'status': 'fail'}
response_object = {'results': user, 'status': 'success'}
return make_response(jsonify(response_object)), 404
return jsonify(response_object), 200
