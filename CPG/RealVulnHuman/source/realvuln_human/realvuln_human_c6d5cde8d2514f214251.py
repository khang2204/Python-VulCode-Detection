try:
    jsonschema.validate(request_data, update_email_schema)
except:
    return Response(error_message_helper("Please provide a proper JSON body."), 400, mimetype="application/json")
resp = token_validator(request.headers.get('Authorization'))
if "error" in resp:
    return Response(error_message_helper(resp), 401, mimetype="application/json")
else:
    user = User.query.filter_by(username=resp['sub']).first()
    if vuln:  # Regex DoS
        match = re.search(
            r"^([0-9a-zA-Z]([-.\w]*[0-9a-zA-Z])*@{1}([0-9a-zA-Z][-\w]*[0-9a-zA-Z]\.)+[a-zA-Z]{2,9})$",
            str(request_data.get('email')))
        if match:
            user.email = request_data.get('email')
            db.session.commit()
            responseObject = {
                'status': 'success',
                'data': {
                    'username': user.username,
                    'email': user.email
                }
            }
