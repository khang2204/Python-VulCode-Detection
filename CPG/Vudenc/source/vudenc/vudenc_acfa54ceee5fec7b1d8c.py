def delete(self, user_id=None):...
post_data = request.get_json(force=True)
Table.delete(user_id, post_data)
response_object = {'status': 'success', 'message': 'User deleted successfully.'
    }
return make_response(jsonify(response_object)), 200
