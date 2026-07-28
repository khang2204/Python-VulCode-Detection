from flask import request
import jwt
import re
import os
from base64 import b64encode, b64decode
import HybridRSA
SERVER_JWT_PRIVATE_KEY = open('resources/jwt_key', 'rb').read()
SERVER_JWT_PUBLIC_KEY = open('resources/jwt_key.pub', 'rb').read()
CREATED = 201
BAD_REQUEST = 400
NOT_FOUND = 404
KEY_SIZE_LIMIT = int(10000.0)
def getKey(client):...
"""docstring"""
validateClient(client)
client_pub_key = loadClientRSAKey(client)
token_data = decodeRequestToken(request.data, client_pub_key)
if re.search('[^a-zA-Z0-9]', token_data['key']):
keytoken = packJWT({'key': requested_key}, SERVER_JWT_PRIVATE_KEY,
    client_pub_key)
requested_key = open('keys/%s/%s.key' % (client, token_data['key']), 'r').read(
    )
return keytoken
