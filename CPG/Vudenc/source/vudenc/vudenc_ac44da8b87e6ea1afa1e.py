def __init__(self, comp_name):...
"""docstring"""
super(LocalCrashEvent, self).__init__(comp_name)
self.message = 'Component %s crashed on localhost' % comp_name
