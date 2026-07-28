def on_caprate_limit(self, rate):...
if not self.logined:
self._capdata = 0, 0
self.log.warning('Caprate limit reached, calling dologin() for now')
return
self.dologin()
