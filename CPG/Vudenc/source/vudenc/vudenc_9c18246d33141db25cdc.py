def _keepalive(self):...
"""docstring"""
now = time.time()
to_remove = []
keep_alives = ((csessid, remove) for csessid, (t, remove) in self.
    last_alive.iteritems() if now - t > _KEEPALIVE)
for csessid, remove in keep_alives:
if remove:
for csessid in to_remove:
to_remove.append(csessid)
self.last_alive[csessid] = now, True
sessions = self.sessionhandler.sessions_from_csessid(csessid)
self.lineSend(csessid, ['ajax_keepalive', [], {}])
for sess in sessions:
sess.disconnect()
self.last_alive.pop(csessid, None)
if not self.last_alive:
self.keep_alive.stop()
self.keep_alive = None
