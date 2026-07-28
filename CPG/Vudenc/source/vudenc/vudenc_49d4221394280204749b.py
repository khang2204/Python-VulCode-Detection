def start(self):...
"""docstring"""
t = threading.Thread(target=self._run, name='ray_import_thread')
t.daemon = True
t.start()
