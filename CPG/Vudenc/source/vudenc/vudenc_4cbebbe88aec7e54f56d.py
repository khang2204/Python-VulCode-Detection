def wait_for_files(files, latency_wait=3):...
"""docstring"""
files = list(files)
get_missing = lambda : [f for f in files if not os.path.exists(f)]
missing = get_missing()
if missing:
logger.info('Waiting at most {} seconds for missing files.'.format(
    latency_wait))
for _ in range(latency_wait):
if not get_missing():
return
time.sleep(1)
