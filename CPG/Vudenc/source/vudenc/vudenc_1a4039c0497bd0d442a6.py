def comment_loop(self):...
for t in self.targets:
self.schedule(self.add_comment, (t, self.msgfun()))
if len(self.targets) == 0:
self.schedule(self.scan_targets_loop)
self.schedule(self.comment_loop)
