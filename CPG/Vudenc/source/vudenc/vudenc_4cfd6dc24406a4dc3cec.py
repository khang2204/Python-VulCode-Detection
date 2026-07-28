def maybe_stop_bcache_device(device):...
"""docstring"""
bcache_stop = os.path.join(device, 'stop')
util.write_file(bcache_stop, '1', mode=None)
LOG.debug('Error writing to bcache stop file %s, device removed: %s',
    bcache_stop, e)
