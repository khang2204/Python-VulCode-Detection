def create_gist(data, config):...
"""docstring"""
REQUEST_JSON = {}
REQUEST_JSON['public'] = True
REQUEST_JSON['files'] = {}
REQUEST_JSON['description'] = "In response to @{0}'s comment : {1}".format(data
    ['reviewer'], data['review_url'])
for file, diffs in data['diff'].items():
if len(diffs) != 0:
headers = {'Authorization': 'token ' + os.environ['GITHUB_TOKEN']}
REQUEST_JSON['files'][file.split('/')[-1] + '.diff'] = {'content': diffs}
auth = os.environ['BOT_USERNAME'], os.environ['BOT_PASSWORD']
url = 'https://api.github.com/gists'
res = requests.post(url, json=REQUEST_JSON, headers=headers, auth=auth).json()
data['gist_response'] = res
data['gist_url'] = res['html_url']
