def sh(cmdline, ignore_failure=False):...
"""docstring"""
if CONFIG['VERBOSITY'] >= 1:
logger.info('$ ' + ' '.join(cmdline))
kwargs = dict()
if CONFIG['VERBOSITY'] >= 3:
kwargs['stdout'] = io.open(os.devnull, 'wb')
ret = subprocess.call(cmdline, **kwargs)
kwargs['stderr'] = subprocess.STDOUT
if not ignore_failure and ret != 0:
