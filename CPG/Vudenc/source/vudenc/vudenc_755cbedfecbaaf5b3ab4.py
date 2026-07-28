def regex(filepattern):...
f = []
last = 0
wildcards = set()
for match in _wildcard_regex.finditer(filepattern):
f.append(re.escape(filepattern[last:match.start()]))
f.append(re.escape(filepattern[last:]))
wildcard = match.group('name')
f.append('$')
if wildcard in wildcards:
return ''.join(f)
if match.group('constraint'):
wildcards.add(wildcard)
f.append('(?P={})'.format(wildcard))
f.append('(?P<{}>{})'.format(wildcard, match.group('constraint') if match.
    group('constraint') else '.+'))
last = match.end()
