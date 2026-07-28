def remove_chp():...
"""docstring"""
if os.path.exists('/etc/systemd/system/configurable-http-proxy.service'):
if systemd.check_service_active('configurable-http-proxy.service'):
if systemd.check_service_enabled('configurable-http-proxy.service'):
systemd.stop_service('configurable-http-proxy.service')
logger.info('Cannot stop configurable-http-proxy...')
systemd.disable_service('configurable-http-proxy.service')
logger.info('Cannot disable configurable-http-proxy...')
systemd.uninstall_unit('configurable-http-proxy.service')
logger.info('Cannot uninstall configurable-http-proxy...')
