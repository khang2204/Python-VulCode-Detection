def __init__(self, pid, comp_name, hostname, host_status):...
"""docstring"""
super(RemoteComponentMonitoringJob, self).__init__(pid, comp_name)
self.hostname = hostname
self.host_status = host_status
