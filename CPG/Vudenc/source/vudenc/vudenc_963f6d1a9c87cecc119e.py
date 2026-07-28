def run_pycodestyle(data, config):...
"""docstring"""
headers = {'Authorization': 'token ' + os.environ['GITHUB_TOKEN']}
auth = os.environ['BOT_USERNAME'], os.environ['BOT_PASSWORD']
repository = data['repository']
after_commit_hash = data['after_commit_hash']
author = data['author']
py_files = get_python_files_involved_in_pr(data)
for file in py_files:
filename = file[1:]
url = 'https://raw.githubusercontent.com/{}/{}/{}'
url = url.format(repository, after_commit_hash, file)
r = requests.get(url, headers=headers, auth=auth)
file_to_check.write(r.text)
cmd = 'pycodestyle {config[pycodestyle_cmd_config]} file_to_check.py'.format(
    config=config)
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
stdout, _ = proc.communicate()
data['extra_results'][filename] = stdout.decode(r.encoding).splitlines()
data['results'][filename] = []
for error in list(data['extra_results'][filename]):
if re.search('^file_to_check.py:\\d+:\\d+:\\s[WE]\\d+\\s.*', error):
for error in list(data['results'][filename]):
data['results'][filename].append(error.replace('file_to_check.py', filename))
if config['scanner']['diff_only']:
url = 'https://github.com/{}/blob/{}{}'
data['extra_results'][filename].remove(error)
if not int(error.split(':')[1]) in py_files[file]:
data[filename + '_link'] = url.format(repository, after_commit_hash, file)
data['results'][filename].remove(error)
os.remove('file_to_check.py')
