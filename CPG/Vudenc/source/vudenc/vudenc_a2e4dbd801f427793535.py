def create_pr(data):...
headers = {'Authorization': 'token ' + os.environ['GITHUB_TOKEN']}
auth = os.environ['BOT_USERNAME'], os.environ['BOT_PASSWORD']
url = 'https://api.github.com/repos/{}/pulls'
url = url.format(data['target_repo_fullname'])
request_json = {'title': 'Fix pep8 errors', 'head': 'pep8speaks:{}'.format(
    data['new_branch']), 'base': data['target_repo_branch'], 'body':
    'The changes are suggested by autopep8'}
r = requests.post(url, json=request_json, headers=headers, auth=auth)
if r.status_code == 201:
data['pr_url'] = r.json()['html_url']
data['error'] = 'Pull request could not be created'
