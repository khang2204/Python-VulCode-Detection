'data': {
                'username': user.username,
                'email': user.email
            }
        }
        return Response(json.dumps(responseObject), 204, mimetype="application/json")
    else:
        return Response(error_message_helper("Please Provide a valid email address."), 400,
                        mimetype="application/json")
else:
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, request_data.get('email'))):
        user.email = request_data.get('email')
        db.session.commit()
        responseObject = {
            'status': 'success',
            'data': {
                'username': user.username,
                'email': user.email
            }
        }
        return Response(json.dumps(responseObject), 204, mimetype="application/json")
