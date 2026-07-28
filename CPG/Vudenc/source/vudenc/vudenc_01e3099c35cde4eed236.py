def remove_observers(self):...
for timer in self.observertimers.values():
timer.cancel()
self.observerscache = {}
self.observertimers = {}
self.observers = []
