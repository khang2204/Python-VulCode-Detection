def wait_loop(self):...
if len(self.targets) > 0:
self.schedule(self.comment_loop)
if len(self.forums) == 0:
return
while len(self.forums) == 0:
self.schedule(self.scan_targets_loop)
self.counter_tick()
self.w.sleep(1)
