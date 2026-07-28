def scan_git_tree(tree):...
for el in tree.traverse():
if el.path.startswith('LICENSES'):
if el.path.find('license-rules.rst') >= 0:
if not os.path.isfile(el.path):
parser.parse_lines(fd, args.maxlines, el.path)
