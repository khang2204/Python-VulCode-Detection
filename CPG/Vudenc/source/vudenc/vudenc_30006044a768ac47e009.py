def wipe_superblock(device):...
"""docstring"""
blockdev = block.sysfs_to_devpath(device)
if block.is_extended_partition(blockdev):
LOG.info("extended partitions do not need wiping, so skipping: '%s'", blockdev)
for bcache_path in ['bcache', 'bcache/set']:
stop_path = os.path.join(device, bcache_path)
retries = [1, 3, 5, 7]
if os.path.exists(stop_path):
LOG.info('wiping superblock on %s', blockdev)
LOG.debug('Attempting to release bcache layer from device: %s', device)
for attempt, wait in enumerate(retries):
maybe_stop_bcache_device(stop_path)
LOG.debug('wiping %s attempt %s/%s', blockdev, attempt + 1, len(retries))
block.wipe_volume(blockdev, mode='superblock')
if attempt + 1 >= len(retries):
LOG.debug('successfully wiped device %s on attempt %s/%s', blockdev, 
    attempt + 1, len(retries))
LOG.debug(
    "wiping device '%s' failed on attempt %s/%s.  sleeping %ss before retry",
    blockdev, attempt + 1, len(retries), wait)
return
time.sleep(wait)
