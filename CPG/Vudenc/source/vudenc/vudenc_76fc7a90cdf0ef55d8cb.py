def set_log(self, *logs, **kwlogs):...
for item in logs:
self._set_log_item(item)
for name, item in kwlogs.items():
self._set_log_item(item, name=name)
