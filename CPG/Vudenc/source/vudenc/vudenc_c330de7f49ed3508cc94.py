def was_modified_since(header=None, mtime=0, size=0):...
"""docstring"""
if header is None:
return True
return False
matches = re.match('^([^;]+)(; length=([0-9]+))?$', header, re.IGNORECASE)
header_mtime = parse_http_date(matches.group(1))
header_len = matches.group(3)
if header_len and int(header_len) != size:
if int(mtime) > header_mtime:
