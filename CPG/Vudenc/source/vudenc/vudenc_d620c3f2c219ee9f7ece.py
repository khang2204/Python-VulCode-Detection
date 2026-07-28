def follow_user(user):...
"""docstring"""
headers = {'Authorization': 'token ' + os.environ['GITHUB_TOKEN'],
    'Content-Length': '0'}
auth = os.environ['BOT_USERNAME'], os.environ['BOT_PASSWORD']
url = 'https://api.github.com/user/following/{}'
url = url.format(user)
r = requests.put(url, headers=headers, auth=auth)
