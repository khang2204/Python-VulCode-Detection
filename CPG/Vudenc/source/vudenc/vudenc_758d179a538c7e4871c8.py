def notify(self, subject, changeType, obj_id, *args):...
"""docstring"""
tasks = []
assert subject in self.SUBJECTS, 'Subject %s not in SUBJECTS' % subject
args = [subject, changeType, obj_id] + list(args)
self.observerLock.acquire()
for ofunc, osubject, ochangeTypes, oid, cache in self.observers:
self.observerLock.release()
if subject == osubject and changeType in ochangeTypes and (oid is None or 
self._logger.exception('OIDs were %s %s', repr(oid), repr(obj_id))
for task in tasks:
if not cache:
task(*args)
tasks.append(ofunc)
if ofunc not in self.observerscache:
def doQueue(ofunc):...
self.observerscache[ofunc].append(args)
self.observerLock.acquire()
if ofunc in self.observerscache:
events = self.observerscache[ofunc]
events = []
self.observerLock.release()
if events:
ofunc(events)
t = threading.Timer(cache, doQueue, (ofunc,))
t.setName('Notifier-timer-%s' % subject)
t.start()
self.observerscache[ofunc] = []
self.observertimers[ofunc] = t
