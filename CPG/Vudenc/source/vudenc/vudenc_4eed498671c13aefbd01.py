def post(self):...
"""docstring"""
"""
        # Check the request comes from appropriate location.
        if not utils.validate_ip(request.remote_addr)
            return {}, 403
        """
INSTITUTION_CODE = 'northwood'
username = request.json.get('username')
firstname = request.json.get('firstName')
lastname = request.json.get('lastName')
password = request.json.get('password')
bio = request.json.get('bio')
institution_code = request.json.get('institutionCode')
if institution_code != INSTITUTION_CODE:
return {'response': 'incorrect institution code'}, 400
if not (username.isalnum() or firstname.isalnum() or lastname.isalnum()):
return {'response': 'incorrect'}, 400
posted = db_interac.add_user(username, firstname, lastname, bio, password)
if posted:
result = db_interac.get_user_profiles()
return {}, 500
if not result:
return {}, 500
response_obj = []
for user in result:
response_obj.append({'id': user[0], 'username': user[1], 'firstName': user[
    2], 'lastName': user[3], 'bio': user[4]})
return response_obj, 201
