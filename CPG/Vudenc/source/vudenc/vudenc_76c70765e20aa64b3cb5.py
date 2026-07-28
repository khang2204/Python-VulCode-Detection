def put(self):...
"""docstring"""
"""
        # Check the request comes from appropriate location.
        if not utils.validate_ip(request.remote_addr)
            return {}, 403
        """
return_obj = False
user_id = request.form.get('userId')
firstname = request.form.get('firstName')
lastname = request.form.get('lastName')
username = request.form.get('username')
password = request.form.get('password')
bio = request.form.get('bio')
print(user_id)
print(firstname)
print(lastname)
"""
        Need to work around nonetype and isalnum()

        if fistname == None:
            temp1 = ""
        if lastname == None:
            temp2 = ""
        if username == None:
            temp3 = ""

        Then check if temp 1, 2 or 3 are alphanumeric
        """
if not (firstname.isalnum() and lastname.isalnum() and username.isalnum()):
return {'response': False}, 400
updated = db_interac.update_profile(user_id, firstname, lastname, username,
    password, bio)
return {'response': updated}, 200 if updated else 400
