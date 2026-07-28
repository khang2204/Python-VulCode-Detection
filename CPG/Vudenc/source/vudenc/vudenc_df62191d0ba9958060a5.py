def create_or_update_comment(data, comment):...
comment_mode = None
headers = {'Authorization': 'token ' + os.environ['GITHUB_TOKEN']}
auth = os.environ['BOT_USERNAME'], os.environ['BOT_PASSWORD']
query = 'https://api.github.com/repos/{}/issues/{}/comments'
query = query.format(data['repository'], str(data['pr_number']))
comments = requests.get(query, headers=headers, auth=auth).json()
last_comment_id = None
for old_comment in comments:
if old_comment['user']['id'] == 24736507:
if last_comment_id is None:
last_comment_id = old_comment['id']
response = requests.post(query, json={'body': comment}, headers=headers,
    auth=auth)
utc_time = datetime.datetime.utcnow()
data['comment_response'] = response.json()
time_now = utc_time.strftime('%B %d, %Y at %H:%M Hours UTC')
comment += """

##### Comment last updated on {}"""
comment = comment.format(time_now)
query = 'https://api.github.com/repos/{}/issues/comments/{}'
query = query.format(data['repository'], str(last_comment_id))
response = requests.patch(query, json={'body': comment}, headers=headers,
    auth=auth)
