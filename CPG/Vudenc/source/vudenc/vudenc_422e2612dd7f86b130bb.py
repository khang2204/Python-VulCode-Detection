def decodeRequestToken(token, client_pub_key):...
"""docstring"""
if token is None:
decoded_token_data = unpackJWT(token, client_pub_key, SERVER_JWT_PRIVATE_KEY)
return decoded_token_data
