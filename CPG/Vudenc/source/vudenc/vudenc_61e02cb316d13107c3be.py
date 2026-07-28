def spawn_nworkers(self, type_, fun, count, args=(), kvargs={}):...
wname = str(fun.__name__)
self.log.info('Starting %s(s)', wname)
if type_ == 0:
if not hasattr(self, 'th_sock'):
if type_ == 1:
self.init_th_sock()
if not hasattr(self, 'th_back_sock'):
if not hasattr(self, 'pr_sock'):
for i in range(count):
self.init_th_back_sock()
self.init_pr_sock()
if not hasattr(self, 'pr_back_sock'):
if not self.running.is_set():
self.init_pr_back_sock()
if type_ == 0:
self.log.exception('Exception "%s" raised on %s spawn', e, wname)
w = workers.WZWorkerThread(self.c.router_addr, fun, args, kvargs, name='.'.
    join((wname, 'th{0}'.format(i))))
if type_ == 1:
self.threads.append(w)
w = workers.WZWorkerProcess(self.c.router_addr, fun, args, kvargs, name='.'
    .join((wname, 'pr{0}'.format(i))))
w.start(self.p.ctx, self.th_sa)
self.processes.append(w)
w.start(self.pr_sa)
