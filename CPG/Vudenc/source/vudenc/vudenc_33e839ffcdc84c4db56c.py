def append_body(self, dom: str):...
"""docstring"""
self.flush_stdout()
self.body.append(dom)
self._last_update_time = time.time()
