def __init__(self, comp_name, hostname):...
"""docstring"""
super(RemoteCrashEvent, self).__init__(comp_name)
self.hostname = hostname
self.message = 'Component %s crashed on remote host %s' % (comp_name, hostname)
