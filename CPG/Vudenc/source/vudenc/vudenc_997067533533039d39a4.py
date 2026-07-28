def fork_for_pr(data):...
FORKED = False
url = 'https://api.github.com/repos/{}/forks'
url = url.format(data['target_repo_fullname'])
headers = {'Authorization': 'token ' + os.environ['GITHUB_TOKEN']}
auth = os.environ['BOT_USERNAME'], os.environ['BOT_PASSWORD']
r = requests.post(url, headers=headers, auth=auth)
if r.status_code == 202:
data['fork_fullname'] = r.json()['full_name']
data['error'] = 'Unable to fork'
FORKED = True
return FORKED
