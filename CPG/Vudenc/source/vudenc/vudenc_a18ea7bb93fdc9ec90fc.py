def get_config(data):...
"""docstring"""
config = {'message': {'opened': {'header': '', 'footer': ''}, 'updated': {
    'header': '', 'footer': ''}}, 'scanner': {'diff_only': False},
    'pycodestyle': {'ignore': [], 'max-line-length': 79, 'count': False,
    'first': False, 'show-pep8': False, 'filename': [], 'exclude': [],
    'select': [], 'show-source': False, 'statistics': False, 'hang-closing':
    False}, 'no_blank_comment': True, 'only_mention_files_with_errors': True}
headers = {'Authorization': 'token ' + os.environ['GITHUB_TOKEN']}
auth = os.environ['BOT_USERNAME'], os.environ['BOT_PASSWORD']
url = 'https://raw.githubusercontent.com/{}/{}/.pep8speaks.yml'
url = url.format(data['repository'], data['after_commit_hash'])
r = requests.get(url, headers=headers, auth=auth)
if r.status_code == 200:
arguments = []
new_config = yaml.load(r.text)
confs = config['pycodestyle']
config = update_dict(config, new_config)
for key, value in confs.items():
if value:
config['pycodestyle_cmd_config'] = ' {arguments}'.format(arguments=' '.join
    (arguments))
if isinstance(value, int):
config['pycodestyle']['ignore'] = [e.upper() for e in list(config[
    'pycodestyle']['ignore'])]
if isinstance(value, bool):
if isinstance(value, list):
return config
arguments.append('--{}'.format(key))
arguments.append('--{}={}'.format(key, value))
arguments.append('--{}={}'.format(key, ','.join(value)))
