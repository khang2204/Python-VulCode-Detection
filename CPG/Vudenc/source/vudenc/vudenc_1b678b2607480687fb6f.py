def update_fork_desc(data):...
url = 'https://api.github.com/repos/{}'.format(data['fork_fullname'])
headers = {'Authorization': 'token ' + os.environ['GITHUB_TOKEN']}
auth = os.environ['BOT_USERNAME'], os.environ['BOT_PASSWORD']
r = requests.get(url, headers=headers, auth=auth)
ATTEMPT = 0
while r.status_code != 200:
time.sleep(5)
full_name = data['target_repo_fullname']
r = requests.get(url, headers=headers, auth=auth)
author, name = full_name.split('/')
ATTEMPT += 1
request_json = {'name': name, 'description': "Forked from @{}'s {}".format(
    author, full_name)}
if ATTEMPT > 10:
r = requests.patch(url, data=json.dumps(request_json), headers=headers,
    auth=auth)
data['error'] = 'Forking is taking more than usual time'
if r.status_code != 200:
data['error'] = 'Could not update description of the fork'
