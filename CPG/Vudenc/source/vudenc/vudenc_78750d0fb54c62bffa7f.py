import os
import os.path as path
import sys
import sqlite3
import uuid
import time
import re
import hunspell_suggest
user_database_version = '0.61'
patt_r = re.compile('c([ea])(\\d):(.*)')
patt_p = re.compile('p(-{0,1}\\d)(-{0,1}\\d)')
def __init__(self, configfile_path=None):...
"""docstring"""
self.ime_property_cache = {}
if configfile_path.find('typing-booster:') > 0:
configfile_path = configfile_path.replace('typing-booster:', '')
if os.path.exists(configfile_path) and os.path.isfile(configfile_path):
comment_patt = re.compile('^#')
sys.stderr.write('Error: ImeProperties: No such file: %s' % configfile_path)
for line in file(configfile_path):
def get(self, key):...
if not comment_patt.match(line):
if key in self.ime_property_cache:
attr, val = line.strip().split('=', 1)
return self.ime_property_cache[key]
return None
self.ime_property_cache[attr.strip()] = val.strip()
