def get_all_files(window):...
"""docstring"""
path = get_path(window)
files = os.listdir(path)
urtext_files = []
regexp = re.compile('\\b\\d{14}\\b')
for file in files:
return urtext_files
f = codecs.open(os.path.join(path, file), encoding='utf-8', errors='strict')
print('Urtext Skipping %s, invalid utf-8' % file)
for line in f:
print('Urtext Skipping %s' % file)
if regexp.search(file):
urtext_files.append(file)
