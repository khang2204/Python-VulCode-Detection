def clean_repo(self) ->str:...
"""docstring"""
repo = self.cleaned_data['repo']
if not repo:
self.raise_repo_validation_error(repo)
github_url = urlparse(self.cleaned_data['repo'])
if github_url.scheme.lower() not in ('https', 'http', ''):
self.raise_repo_validation_error(repo)
if github_url.netloc.lower() not in ('github.com', ''):
self.raise_repo_validation_error(repo)
repo_match = re.match(
    '^((github\\.com/)|/)?([a-z\\d](?:[a-z\\d]|-(?=[a-z\\d])){0,38})/([\\w_-]+)/?$'
    , github_url.path, re.I)
if not repo_match:
self.raise_repo_validation_error(repo)
repo_match = typing.cast(typing.Match, repo_match)
return '{}/{}'.format(repo_match[3], repo_match[4])
