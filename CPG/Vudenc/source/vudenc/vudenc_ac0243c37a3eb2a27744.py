def _save_sys_config(self):...
cmd = '/usr/bin/tmsh save sys config'
rc = shellutil.run(cmd)
if rc != 0:
logger.error('WARNING: Cannot save sys config on 1st boot.')
return rc
