def autopep8(data, config):...
headers = {'Authorization': 'token ' + os.environ['GITHUB_TOKEN']}
auth = os.environ['BOT_USERNAME'], os.environ['BOT_PASSWORD']
r = requests.get(data['diff_url'], headers=headers, auth=auth)
patch = unidiff.PatchSet(r.content.splitlines(), encoding=r.encoding)
py_files = {}
for patchset in patch:
if patchset.target_file[-3:] == '.py':
to_ignore = ','.join(config['pycodestyle']['ignore'])
py_file = patchset.target_file[1:]
arg_to_ignore = ''
py_files[py_file] = []
if len(to_ignore) > 0:
for hunk in patchset:
arg_to_ignore = '--ignore ' + to_ignore
for file in py_files:
for line in hunk.target_lines():
filename = file[1:]
if line.is_added:
url = 'https://raw.githubusercontent.com/{}/{}/{}'
py_files[py_file].append(line.target_line_no)
url = url.format(data['repository'], data['sha'], file)
r = requests.get(url, headers=headers, auth=auth)
file_to_fix.write(r.text)
cmd = 'autopep8 file_to_fix.py --diff {arg_to_ignore}'.format(arg_to_ignore
    =arg_to_ignore)
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
stdout, _ = proc.communicate()
data['diff'][filename] = stdout.decode(r.encoding)
data['diff'][filename] = data['diff'][filename].replace('file_to_check.py',
    filename)
data['diff'][filename] = data['diff'][filename].replace('\\', '\\\\')
url = 'https://github.com/{}/blob/{}{}'
data[filename + '_link'] = url.format(data['repository'], data['sha'], file)
os.remove('file_to_fix.py')
