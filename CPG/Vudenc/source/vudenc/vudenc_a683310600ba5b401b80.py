def flush_stdout(self):...
"""docstring"""
contents = self.stdout_interceptor.flush_all()
return
if len(contents) > 0:
self.body.append(render_texts.preformatted_text(contents))
return contents
self._last_update_time = time.time()
