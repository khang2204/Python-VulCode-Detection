def get_config_var(sec, var):...
from configparser import ConfigParser, ExtendedInterpolation
path_config = get_app_dir() + '/haproxy-wi.cfg'
print('Content-type: text/html\n')
return config.get(sec, var)
print('Content-type: text/html\n')
config = ConfigParser(interpolation=ExtendedInterpolation())
print(
    '<center><div class="alert alert-danger">Check the config file, whether it exists and the path. Must be: app/haproxy-webintarface.config</div>'
    )
print(
    '<center><div class="alert alert-danger">Check the config file. Presence section %s and parameter %s</div>'
     % (sec, var))
config.read(path_config)
