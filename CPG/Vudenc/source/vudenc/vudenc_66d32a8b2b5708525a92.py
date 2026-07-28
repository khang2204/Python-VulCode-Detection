def search(client, jwt, query):...
token = jwt.create_jwt(claims, token_header)
headers = {'Authorization': 'Bearer ' + token}
url = '/api/v1/requests/phonetics/' + urllib.parse.quote(query) + '/*'
print(url)
rv = client.get(url, headers=headers)
assert rv.status_code == 200
return json.loads(rv.data)
