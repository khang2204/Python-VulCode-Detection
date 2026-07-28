'''
You will need to authenticate to this URI first. You will need to pass a JSON body with a username and password key.
If you enter a valid username and password, a JWT token is returned in the HTTP Response in the Authorization header.
This token can be used for subsequent requests.
'''
try:
    content = request.json
    print(content)
    username = content['username']
    password = content['password']
    auth_user = User.query.filter_by(username = username, password = password).first()
    if auth_user:
        auth_token = jwt.encode({'user': username, 'exp': get_exp_date(), 'nbf': datetime.datetime.utcnow(), 'iss': 'we45', 'iat': datetime.datetime.utcnow()}, app.config['SECRET_KEY_HMAC'], algorithm='HS256')
        resp = Response(json.dumps({'Authenticated': True, "User": username}))
        #resp.set_cookie('SESSIONID', auth_token)
        resp.headers['Authorization'] = "{0}".format(auth_token)
        resp.status_code = 200
        resp.mimetype = 'application/json'
        return resp
    else:
        return jsonify({'Error': 'No User here...'}),404
