@jwt_required...
if instance_id:
query = {'instance_id': instance_id, 'user_id': user_id}
response_object = {'results': Table.query(), 'status': 'success'}
results = Table.filter_by(**query)
return jsonify(response_object), 200
if len(results) < 1:
response_object = {'results': 'Instance not found', 'status': 'error'}
response_object = {'results': results, 'status': 'success'}
return make_response(jsonify(response_object)), 404
return jsonify(response_object), 200
