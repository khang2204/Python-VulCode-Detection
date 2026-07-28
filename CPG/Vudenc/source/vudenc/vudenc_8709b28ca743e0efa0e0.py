def create_new_branch(data):...
url = 'https://api.github.com/repos/{}/git/refs/heads'
url = url.format(data['fork_fullname'])
headers = {'Authorization': 'token ' + os.environ['GITHUB_TOKEN']}
auth = os.environ['BOT_USERNAME'], os.environ['BOT_PASSWORD']
sha = None
r = requests.get(url, headers=headers, auth=auth)
for ref in r.json():
if ref['ref'].split('/')[-1] == data['target_repo_branch']:
url = 'https://api.github.com/repos/{}/git/refs'
sha = ref['object']['sha']
url = url.format(data['fork_fullname'])
data['new_branch'] = '{}-pep8-patch'.format(data['target_repo_branch'])
request_json = {'ref': 'refs/heads/{}'.format(data['new_branch']), 'sha': sha}
r = requests.post(url, json=request_json, headers=headers, auth=auth)
if r.status_code != 200:
data['error'] = 'Could not create new branch in the fork'
