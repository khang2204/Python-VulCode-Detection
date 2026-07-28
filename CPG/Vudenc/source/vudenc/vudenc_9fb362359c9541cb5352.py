def glob_wildcards(pattern):...
"""docstring"""
pattern = os.path.normpath(pattern)
first_wildcard = re.search('{[^{]', pattern)
dirname = os.path.dirname(pattern[:first_wildcard.start()]
    ) if first_wildcard else os.path.dirname(pattern)
if not dirname:
dirname = '.'
names = [match.group('name') for match in _wildcard_regex.finditer(pattern)]
Wildcards = namedtuple('Wildcards', names)
wildcards = Wildcards(*[list() for name in names])
pattern = re.compile(regex(pattern))
for dirpath, dirnames, filenames in os.walk(dirname):
for f in chain(filenames, dirnames):
return wildcards
if dirpath != '.':
f = os.path.join(dirpath, f)
match = re.match(pattern, f)
if match:
for name, value in match.groupdict().items():
getattr(wildcards, name).append(value)
