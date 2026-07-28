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
