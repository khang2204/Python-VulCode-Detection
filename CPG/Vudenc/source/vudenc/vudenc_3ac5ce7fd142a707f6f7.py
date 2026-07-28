def post(self):...
"""docstring"""
"""
        # Check the request comes from appropriate location.
        if not utils.validate_ip(request.remote_addr)
            return {}, 403
        """
message = request.form.get('content')
timeposted = request.form.get('timePosted')
eventtime = request.form.get('eventTime')
poster_id = request.form.get('userId')
poster_username = request.form.get('username')
poster_firstname = request.form.get('firstName')
poster_lastname = request.form.get('lastName')
response = db_interac.add_message(message, timeposted, eventtime, poster_id,
    poster_username, poster_firstname, poster_lastname)
if response:
response = db_interac.get_messages(1)
return {'response': response}, 500
return response, 201
