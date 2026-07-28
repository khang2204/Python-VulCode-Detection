def _load_yml_filedir(path):...
"""docstring"""
YML_FILE_SUFFIX = '.yml'
bpath = os.path.basename(path)
if os.path.isdir(path):
result = {}
if os.path.isfile(path):
for entry in os.listdir(path):
if os.path.abspath(path) == os.path.abspath(sys.argv[0]):
epath = os.path.join(path, entry)
return bpath, result
return None, None
if path.endswith(YML_FILE_SUFFIX):
key, value = _load_yml_filedir(epath)
bpath = bpath[:-len(YML_FILE_SUFFIX)]
return None, None
if not key:
return bpath, yaml.load(open(path))
return bpath, None
result[key] = value
