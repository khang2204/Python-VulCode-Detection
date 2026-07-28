def __init__(self, configfile_path=None):...
"""docstring"""
self.ime_property_cache = {}
if configfile_path.find('typing-booster:') > 0:
configfile_path = configfile_path.replace('typing-booster:', '')
if os.path.exists(configfile_path) and os.path.isfile(configfile_path):
comment_patt = re.compile('^#')
sys.stderr.write('Error: ImeProperties: No such file: %s' % configfile_path)
for line in file(configfile_path):
if not comment_patt.match(line):
attr, val = line.strip().split('=', 1)
self.ime_property_cache[attr.strip()] = val.strip()
