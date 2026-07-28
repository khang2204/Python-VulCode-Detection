def __init__(self, settings, debug=False):...
self.settings = settings
self.serial_settings = get_serial_settings(settings)
self.sensors = settings.get('sensors', None)
self.cmd = codecs.decode(self.settings['cmd'], 'unicode-escape')
self.regex = settings.get('regex', None)
self.debug = debug
if self.debug:
print('serial settings:', self.serial_settings)
super().__init__(**self.serial_settings)
