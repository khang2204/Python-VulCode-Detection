def _set_log_item(self, item, name=None):...
if isinstance(item, str) or callable(item):
self.log.append(IOFile(item, rule=self) if isinstance(item, str) else item)
start = len(self.log)
if name:
for i in item:
self.log.add_name(name)
self._set_log_item(i)
if name:
self.log.set_name(name, start, end=len(self.log))
