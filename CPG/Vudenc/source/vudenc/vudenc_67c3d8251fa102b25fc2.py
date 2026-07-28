@utils.synchronized('3par', external=True)...
"""docstring"""
self.common.client_login()
self.common.terminate_connection(volume, connector['host'], connector['wwpns'])
self.common.client_logout()
