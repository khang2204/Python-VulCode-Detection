"""
This script downloads and repacks official rust language builds
with the necessary tool and target support for the Firefox
build environment.
"""
import requests
import toml
import os
def fetch_file(url):...
"""docstring"""
filename = os.path.basename(url)
if os.path.exists(filename):
return
r = requests.get(url, stream=True)
r.raise_for_status()
for chunk in r.iter_content(4096):
fd.write(chunk)
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
def install(filename, target):...
"""docstring"""
print(' Unpacking %s...' % filename)
os.system('tar xf ' + filename)
basename = filename.split('.tar')[0]
print(' Installing %s...' % basename)
install_opts = '--prefix=${PWD}/%s --disable-ldconfig' % target
os.system('%s/install.sh %s' % (basename, install_opts))
print(' Cleaning %s...' % basename)
os.system('rm -rf %s' % basename)
def package(manifest, pkg, target):...
"""docstring"""
version = manifest['pkg'][pkg]['version']
info = manifest['pkg'][pkg]['target'][target]
return version, info
