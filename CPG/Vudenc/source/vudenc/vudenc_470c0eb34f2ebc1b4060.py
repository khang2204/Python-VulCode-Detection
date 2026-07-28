def validate_server_software(page):...
if 'Server' not in page.headers:
return True
server_header = str.lower(page.headers['Server'])
if 'nginx' in server_header or 'apache' in server_header:
return False
return True
