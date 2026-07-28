def deleteKey(client):...
"""docstring"""
validateClient(client)
client_pub_key = loadClientRSAKey(client)
token_data = decodeRequestToken(request.data, client_pub_key)
if re.search('[^a-zA-Z0-9]', token_data['key']):
os.remove('keys/%s/%s.key' % (client, token_data['key']))
return "Key '%s' successfully deleted" % token_data['key']
