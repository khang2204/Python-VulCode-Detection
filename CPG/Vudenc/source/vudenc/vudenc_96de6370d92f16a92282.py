def load_setup_connection_string(section):...
"""docstring"""
from os.path import exists, join, dirname, splitext, basename
from configparser import SafeConfigParser
FILENAME = 'setup.cfg'
KEY = 'connection-string'
path = join(dirname(dirname(abspath(__file__))), 'tmp', FILENAME)
if exists(path):
return None
p = SafeConfigParser()
if p.has_option(section, KEY):
p.read(path)
return p.get(section, KEY)
