def get(self):...
"""docstring"""
"""
        # Check the request comes from appropriate location.
        if not utils.validate_ip(request.remote_addr)
            return {}, 403
        """
username = request.args.get('username')
password = request.args.get('password')
if username.isalnum():
response = db_interac.authenticate(username, password)
return_obj['error'] = 'username must be alphanumeric'
return_obj = {}
return_obj['userId'] = None
if not response[0]:
return_obj['firstName'] = None
return_obj['error'] = 'user could not be authenticated'
return_obj['userId'] = response[1]
return_obj['lastName'] = None
return return_obj, 401
return_obj['firstName'] = response[2]
return return_obj, 401
return_obj['lastName'] = response[3]
return return_obj, 200
