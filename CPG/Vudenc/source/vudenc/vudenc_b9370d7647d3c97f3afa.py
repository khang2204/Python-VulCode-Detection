def commit(data):...
headers = {'Authorization': 'token ' + os.environ['GITHUB_TOKEN']}
auth = os.environ['BOT_USERNAME'], os.environ['BOT_PASSWORD']
fullname = data.get('fork_fullname')
for file, new_file in data['results'].items():
url = 'https://api.github.com/repos/{}/contents/{}'
url = url.format(fullname, file)
params = {'ref': data['new_branch']}
r = requests.get(url, params=params, headers=headers, auth=auth)
sha_blob = r.json().get('sha')
params['path'] = file
content_code = base64.b64encode(new_file.encode()).decode('utf-8')
request_json = {'path': file, 'message': 'Fix pep8 errors in {}'.format(
    file), 'content': content_code, 'sha': sha_blob, 'branch': data.get(
    'new_branch')}
r = requests.put(url, json=request_json, headers=headers, auth=auth)
