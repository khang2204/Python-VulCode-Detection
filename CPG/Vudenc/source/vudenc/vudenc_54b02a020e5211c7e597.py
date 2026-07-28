@app.route('/api', methods=['POST'])...
"""docstring"""
req_data = request.get_json()
verification = verify_proper_post_request(req_data)
if type(verification).__name__ == 'int':
return api_response('error', ERRORS[verification], 400)
user_info = req_data.get('userInfo', None)
all_tasks = req_data.get('allTasks', None)
if user_info is None or all_tasks is None:
return api_response('error', 'Missing required information', 400)
for req in REQUIRED:
if req not in user_info:
all_users = storage.all('User').values()
return api_response('error', 'Missing attribute', 400)
verified_user = None
for user in all_users:
this_fbid = User.text_decrypt(user.fbid)
if verified_user is None:
if verification == this_fbid:
message = initialize_new_task_list(user_info, all_tasks)
message = update_user_tasks(verified_user, all_tasks)
verified_user = user
return api_response('success', message, 200)
return api_response('success', message, 200)
