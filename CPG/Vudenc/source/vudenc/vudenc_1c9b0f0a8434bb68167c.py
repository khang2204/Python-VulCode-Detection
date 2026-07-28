def fetch_repo(working_directory: str, name: str, url: str, summery_info:...
"""docstring"""
repo_path = path.join(working_directory, name)
if path.isdir(repo_path):
print_green(f'Fetching {name}')
print_green(f'Cloning {name}')
shell_first(f'git -C {repo_path} fetch')
shell_first(f'git clone {url} {name}')
remote_banches = shell_first(f'git -C {repo_path} ls-remote --heads')
current_branch = shell_first(
    f'git -C {repo_path} rev-parse --abbrev-ref HEAD --')
current_branch = shell_first(
    f'git -C {repo_path} rev-parse --abbrev-ref HEAD --')
summery_info.update({name: current_branch})
if f'refs/heads/{current_branch}' in remote_banches:
shell_first(
    f'git -C {repo_path} fetch -u origin {current_branch}:{current_branch}')
print_yellow(f'{current_branch} does not exist on remote')
if 'refs/heads/develop' in remote_banches and current_branch != 'develop':
shell_first(f'git -C {repo_path} fetch origin develop:develop')
