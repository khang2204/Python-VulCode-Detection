def create_cluster_archive(self):...
"""docstring"""
self.log_info('Creating archive of sosreports...')
self.create_sos_archive()
if self.archive:
self.logger.info('Archive created as %s' % self.archive)
self.cleanup()
self.console.info(
    """
The following archive has been created. Please provide it to your support team."""
    )
self.console.info('    %s' % self.archive)
