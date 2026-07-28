def get(self):...
"""docstring"""
"""
        # Check the request comes from appropriate location.
        if not utils.validate_ip(request.remote_addr)
            return {}, 403
        """
user_id = request.form.get('userId')
if user_id is None:
users = db_interac.get_user_profiles()
user_profile = db_interac.get_user_profile(user_id)
if not users:
return_obj = {}
return {}, 500
response_obj = []
if user_profile[0] == False:
for user in users:
return_obj['error'] = 'error adding profile'
return_obj['username'] = user_profile[1]
response_obj.append({'id': user[0], 'username': user[1], 'firstName': user[
    2], 'lastName': user[3], 'bio': user[4]})
return response_obj, 200
return return_obj, 200
return_obj['firstName'] = user_profile[2]
return_obj['lastName'] = user_profile[3]
return_obj['bio'] = user_profile[4]
return_obj['messages'] = user_profile[5]
