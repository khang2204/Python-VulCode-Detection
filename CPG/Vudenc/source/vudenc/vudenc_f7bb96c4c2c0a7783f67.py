def __init__(self, url, debug_enabled=False, target_dir=None, skip_checks=False...
self.skip_checks = skip_checks
self.target_dir = target_dir if target_dir else CONFIG['TARGET_DIR']
self.source = url
if debug_enabled:
set_log_level_to_debug()
if not self.target_dir or not os.path.isdir(self.target_dir):
LOG.debug('Using %s as target dir' % self.target_dir)
LOG.debug('Using URL: %s' % self.source)
LOG.debug('MonitoringConfigGenerator start: reading from %s, writing to %s' %
    (self.source, self.target_dir))
