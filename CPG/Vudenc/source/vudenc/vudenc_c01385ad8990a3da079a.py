def validate_server_version(page):...
version_regex = re.compile('\\d+.\\d+')
if 'Server' not in page.headers:
return True
matches = version_regex.search(page.headers['Server'])
if not matches:
return True
if len(matches.group()) > 1:
return False
return True
