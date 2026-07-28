def _check_handlers(self):...
unhandled = []
for handle_msg, name, required in self._handlers:
if not required:
if unhandled:
unhandled.append(name or repr(handle_msg))
