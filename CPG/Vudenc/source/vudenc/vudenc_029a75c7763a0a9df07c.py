def run_check(self):...
"""docstring"""
if self.host_status.get(self.hostname):
cmd = 'ssh -F %s %s "ps -p %s > /dev/null"' % (config.
    CUSTOM_SSH_CONFIG_PATH, self.hostname, self.pid)
return True
if call(cmd, shell=True) == 0:
return True
return RemoteCrashEvent(self.comp_name, self.hostname)
