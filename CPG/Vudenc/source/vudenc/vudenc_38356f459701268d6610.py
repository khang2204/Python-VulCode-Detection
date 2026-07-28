def fetch(url):...
"""docstring"""
base = os.path.basename(url)
print('Fetching %s...' % base)
fetch_file(url + '.asc')
fetch_file(url)
fetch_file(url + '.sha256')
fetch_file(url + '.asc.sha256')
print('Verifying %s...' % base)
os.system('shasum -c %s.sha256' % base)
os.system('shasum -c %s.asc.sha256' % base)
os.system('gpg --verify %s.asc %s' % (base, base))
os.system('keybase verify %s.asc' % base)
