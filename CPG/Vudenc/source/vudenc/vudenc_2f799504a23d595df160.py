def write_both(self, *args, **kwargs):...
abort_thread()
if self.active:
self.last_write_time = time.time()
return self.redirection_source.write(*args, **kwargs)
super(RedirectBuffer, self).write(*args, **kwargs)
