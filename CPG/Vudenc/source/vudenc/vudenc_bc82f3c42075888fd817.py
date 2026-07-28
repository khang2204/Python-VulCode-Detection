def _wait_until_mcpd_is_initialized(self):...
"""docstring"""
for retries in range(1, 100):
logger.info('Checking to see if mcpd is up')
if rc is 0:
rc = shellutil.run(
    '/usr/bin/tmsh -a show sys mcp-state field-fmt 2>/dev/null | grep phase | grep running'
    , chk_err=False)
return True
if rc == 0:
logger.info('mcpd is up!')
time.sleep(30)
