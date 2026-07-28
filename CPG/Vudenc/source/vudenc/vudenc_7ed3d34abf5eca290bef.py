def put(self):...
"""docstring"""
"""
        # Check the request comes from appropriate location.
        if not utils.validate_ip(request.remote_addr)
            return {}, 403
        """
message_id = request.json.get('id')
likes = request.json.get('likes')
comment = request.json.get('comment')
print(message_id)
print(likes)
print(str(comment))
if comment is not None:
if {'content', 'userId', 'username', 'firstname', 'lastname', 'timeposted'
response = db_interac.update_message(message_id, likes, comment)
return {'response': False}, 400
if response == False:
return {'response': response}, 400
return {'response': response}, 200
