def _load_configfile(configpath):...
"""docstring"""
return json.load(f)
f.seek(0)
import yaml
return yaml.load(f)
