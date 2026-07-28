@app.route('/api/<fbid>', methods=['GET'])...
"""docstring"""
if fbid is None:
return api_response('error', 'Unknown id', 401)
all_users = storage.all('User').values()
verified_user = None
for user in all_users:
this_fbid = User.text_decrypt(user.fbid)
if verified_user is None:
if fbid == this_fbid:
return api_response('error', 'Unknown id', 401)
all_tasks = make_todo_list(verified_user)
verified_user = user
return jsonify(all_tasks), 201
