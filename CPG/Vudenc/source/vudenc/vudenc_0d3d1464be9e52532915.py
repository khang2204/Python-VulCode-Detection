def updateKey(client):...
"""docstring"""
validateClient(client)
client_pub_key = loadClientRSAKey(client)
token_data = decodeRequestToken(request.data, client_pub_key)
validateNewKeyData(token_data)
if os.path.isfile('keys/%s/%s.key' % (client, token_data['name'])):
f.write(token_data['key'])
return 'Key successfully updated', CREATED
