def ensure_jupyterhub_running(times=20):...
"""docstring"""
for i in range(times):
logger.info('Waiting for JupyterHub to come up ({}/{} tries)'.format(i + 1,
    times))
if h.code in [404, 502, 503]:
urlopen('http://127.0.0.1')
time.sleep(1)
if isinstance(e.reason, ConnectionRefusedError):
return
time.sleep(1)
