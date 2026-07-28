def __init__(self, filename, debug):...
self._parsed_content_packages = None
self._parsed_status_test_usernames = None
self.section = _CONFIG_SECTION
_CONFIG_DEFAULTS['debug'] = str(debug)
cfgdir = os.path.dirname(filename)
_CONFIG_DEFAULTS['pysaml2_config'] = os.path.join(cfgdir, _CONFIG_DEFAULTS[
    'pysaml2_config'])
self.config = ConfigParser.ConfigParser(_CONFIG_DEFAULTS)
if not self.config.read([filename]):
