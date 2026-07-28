def __init__(self, host_port, device_port, app_name, adb_proxy, log=logging...
"""docstring"""
self.host_port = host_port
self.device_port = device_port
self.app_name = app_name
self.uid = None
self._adb = adb_proxy
self._client = None
self._conn = None
self._counter = None
self._lock = threading.Lock()
self._event_client = None
self._log = log
