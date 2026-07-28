def addKey(client):...
"""docstring"""
validateClient(client)
client_pub_key = loadClientRSAKey(client)
token_data = decodeRequestToken(request.data, client_pub_key)
validateNewKeyData(token_data)
f.write(token_data['key'])
return 'Key successfully created', CREATED
