def translate_options(self, info, options):...
"""docstring"""
ret = {}
if not int(options['simulated-human-interaction']):
ret['human'] = int(options['simulated-human-interaction'])
return emit_options(ret)
