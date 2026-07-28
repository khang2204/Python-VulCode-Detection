def delete_if_forked(data):...
FORKED = False
url = 'https://api.github.com/user/repos'
headers = {'Authorization': 'token ' + os.environ['GITHUB_TOKEN']}
auth = os.environ['BOT_USERNAME'], os.environ['BOT_PASSWORD']
r = requests.get(url, headers=headers, auth=auth)
for repo in r.json():
if repo['description']:
return FORKED
if data['target_repo_fullname'] in repo['description']:
FORKED = True
r = requests.delete('https://api.github.com/repos/{}'.format(repo[
    'full_name']), headers=headers, auth=auth)
