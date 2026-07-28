def comment_permission_check(data, comment):...
"""docstring"""
PERMITTED_TO_COMMENT = True
repository = data['repository']
headers = {'Authorization': 'token ' + os.environ['GITHUB_TOKEN']}
auth = os.environ['BOT_USERNAME'], os.environ['BOT_PASSWORD']
url = 'https://api.github.com/repos/{}/issues/{}/comments'
url = url.format(repository, str(data['pr_number']))
comments = requests.get(url, headers=headers, auth=auth).json()
last_comment = ''
for old_comment in reversed(comments):
if old_comment['user']['id'] == 24736507:
"""
    # Disabling this because only a single comment is made per PR
    text1 = ''.join(BeautifulSoup(markdown(comment)).findAll(text=True))
    text2 = ''.join(BeautifulSoup(markdown(last_comment)).findAll(text=True))
    if text1 == text2.replace("submitting", "updating"):
        PERMITTED_TO_COMMENT = False
    """
last_comment = old_comment['body']
for old_comment in reversed(comments):
if '@pep8speaks' in old_comment['body']:
return PERMITTED_TO_COMMENT
if 'resume' in old_comment['body'].lower():
if 'quiet' in old_comment['body'].lower():
PERMITTED_TO_COMMENT = False
