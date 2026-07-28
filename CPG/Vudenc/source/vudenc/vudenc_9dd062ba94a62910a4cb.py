@jwt_refresh_token_required...
current_user = get_jwt_identity()
access_token = create_access_token(identity=current_user)
resp = jsonify({'refresh': True})
set_access_cookies(resp, access_token)
return resp
