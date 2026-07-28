def doQueue(ofunc):...
self.observerLock.acquire()
if ofunc in self.observerscache:
events = self.observerscache[ofunc]
events = []
self.observerLock.release()
if events:
ofunc(events)
