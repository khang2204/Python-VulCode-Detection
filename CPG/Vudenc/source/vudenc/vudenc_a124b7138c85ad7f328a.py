def stop_server(self):...
if self.test_server:
if hasattr(self.test_server, 'kill'):
self.test_server.kill()
os.kill(self.test_server.pid, signal.SIGKILL)
self.test_server = None
self.port = None
self.url = None
if self.tmp_db:
os.remove(self.tmp_db)
self.tmp_db = None
