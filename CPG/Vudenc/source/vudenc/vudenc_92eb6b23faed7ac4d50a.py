def kill_children():...
"""docstring"""
log.info('Stopping worker(s)')
for pid in child_pids:
if pid is not None:
os.kill(pid, signal.SIGTERM)
