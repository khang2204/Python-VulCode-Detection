def get_device(settings, instrum, debug=False):...
"""docstring"""
if 'device_class' in settings:
device_class = settings['device_class']
if instrum in ['simulate', 'fake']:
mod, obj = device_class.split('.')
device_class = 'fake.Fake'
device_class = 'generic.Generic'
module = import_module('..devices.' + mod, __name__)
return getattr(module, obj)(settings, debug=debug)
