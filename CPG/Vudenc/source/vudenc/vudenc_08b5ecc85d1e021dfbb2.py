@app.route('/json/tweets/search/<query>', methods=['GET'])...
access_token = '487593326-yu9WIClcUgs9vBWJGGgW4QC9pKedHMdm3NhhNoxe'
access_token_secret = 'fMcsDcqTtbeM73qB7Cxo7dGKhZT9byGh7i5lKjOVscQzP'
consumer_key = 'yd6lDwm3Ra9j7djyXHmrg'
consumer_secret = 'BlBMf6kP98LwWepOVSypVwDi2x2782P2KQnJQomY'
oauth = OAuth1(consumer_key, resource_owner_key=access_token,
    resource_owner_secret=access_token_secret, client_secret=consumer_secret)
base_url = 'https://api.twitter.com/1.1/'
search_url = 'search/tweets.json'
verify_url = 'account/verify_credentials.json'
payload = {'q': query, 'count': '5', 'lang': 'en', 'result_type': 'mixed'}
response = requests.get(base_url + verify_url, auth=oauth)
if response.status_code == 200:
response = requests.get(base_url + search_url, params=payload, auth=oauth)
return jsonify(error=str(response.content))
resp = Response(response=response.content, status=200, mimetype=
    'application/json')
return resp
