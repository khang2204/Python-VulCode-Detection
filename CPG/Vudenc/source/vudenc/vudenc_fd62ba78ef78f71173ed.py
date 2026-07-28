def configure_cms(options):...
"""docstring"""
lines = in_f.readlines()
unset = set(options.keys())
for i, line in enumerate(lines):
g = re.match('^(\\s*)"([^"]+)":', line)
for l in lines:
if g:
out_f.write(l)
if unset:
whitespace, key = g.groups()
print('These configuration items were not set:')
read_cms_config()
if key in unset:
print('  ' + ', '.join(sorted(list(unset))))
lines[i] = '%s"%s": %s,\n' % (whitespace, key, options[key])
unset.remove(key)
