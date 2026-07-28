# fetching user data if the user exists
    user = User.query.filter_by(username=request_data.get('username')).first()
    if user and request_data.get('password') == user.password:
        auth_token = user.encode_auth_token(user.username)
        responseObject = {
            'status': 'success',
            'message': 'Successfully logged in.',
            'auth_token': auth_token
        }
        return Response(json.dumps(responseObject), 200, mimetype="application/json")
    if vuln:  # Password Enumeration
        if user and request_data.get('password') != user.password:
            return Response(error_message_helper("Password is not correct for the given username."), 200,
                            mimetype="application/json")
        elif not user:  # User enumeration
            return Response(error_message_helper("Username does not exist"), 200, mimetype="application/json")
    else:
        if (user and request_data.get('password') != user.password) or (not user):
            return Response(error_message_helper("Username or Password Incorrect!"), 200,
                            mimetype="application/json")
except jsonschema.exceptions.ValidationError as exc:
    return Response(error_message_helper(exc.message), 400, mimetype="application/json")
except:
    return Response(error_message_helper("An error occurred!"), 200, mimetype="application/json")
