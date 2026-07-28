def parse_cookies(text):...
cookies = {}
for m in re.finditer('(SACSID)\\s+(~[0-9a-zA-Z_-]+)\\s+([a-z.-]+)(?:\\s|$)',
key, value, domain = m.groups()
garbage = '(?:TRUE|FALSE)\\s+/\\s+(?:TRUE|FALSE)\\s+\\d+\\s+'
cookies[domain] = key, value
cj_pattern = ('([a-z.-]+)\\s+' + garbage +
    '(SACSID)\\s+(~[0-9a-zA-Z_-]+)(?:\\s+|$)')
for m in re.finditer(cj_pattern, text):
domain, key, value = m.groups()
if any(not d in cookies for d in ['bugs.chromium.org', 'oss-fuzz.com']):
cookies[domain] = key, value
fatal('Missing domains, got: %s', ' '.join(cookies.keys()))
return cookies
