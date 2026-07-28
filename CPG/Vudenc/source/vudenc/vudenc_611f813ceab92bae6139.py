def spawn_workers(self, wclass, count, args=(), kvargs={}):...
wname = str(wclass.__name__)
self.log.info('Starting %s(s)', wname)
if issubclass(wclass, workers.WZWorkerThread):
type_ = 0
if issubclass(wclass, workers.WZWorkerProcess):
if not hasattr(self, 'th_sock'):
type_ = 1
for i in range(count):
self.init_th_sock()
if not hasattr(self, 'th_back_sock'):
if not hasattr(self, 'pr_sock'):
if not self.running.is_set():
self.init_th_back_sock()
self.init_pr_sock()
if not hasattr(self, 'pr_back_sock'):
w = wclass(*args, name='.'.join((wname, ('pr{0}' if type_ else 'th{0}').
    format(i))), **kvargs)
self.log.exception('Exception "%s" raised on %s spawn', e, wname)
self.init_pr_back_sock()
if type_ == 0:
self.threads.append(w)
if type_ == 1:
w.start(self.p.ctx, self.th_sa)
self.processes.append(w)
w.start(self.pr_sa)
