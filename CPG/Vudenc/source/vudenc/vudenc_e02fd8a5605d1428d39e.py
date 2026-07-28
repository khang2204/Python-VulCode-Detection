def get_files_involved_in_pr(data):...
"""docstring"""
headers = {'Authorization': 'token ' + os.environ['GITHUB_TOKEN']}
diff_headers = headers.copy()
diff_headers['Accept'] = 'application/vnd.github.VERSION.diff'
auth = os.environ['BOT_USERNAME'], os.environ['BOT_PASSWORD']
repository = data['repository']
after_commit_hash = data['after_commit_hash']
author = data['author']
diff_url = 'https://api.github.com/repos/{}/pulls/{}'
diff_url = diff_url.format(repository, str(data['pr_number']))
r = requests.get(diff_url, headers=diff_headers, auth=auth)
patch = unidiff.PatchSet(r.content.splitlines(), encoding=r.encoding)
files = {}
for patchset in patch:
file = patchset.target_file[1:]
return files
files[file] = []
for hunk in patchset:
for line in hunk.target_lines():
if line.is_added:
files[file].append(line.target_line_no)
