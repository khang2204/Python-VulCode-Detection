def __call__(self, parent):...
self.p = parent
self.log = parent.log
self.inter_sleep = parent.inter_sleep
self.running = parent.running
self.p.sig_sock.setsockopt(zmq.SUBSCRIBE, b'WipeManager')
self.p.wz.set_sig_handler(b'WipeManager', b'passthrough', self.send_passthrough
    )
if self.c.tcount > 0:
self.pc = ProcessContext(self.p.name, self.p.ctx, self.c.router_addr,
    noproxy_rp)
if self.c.ecount > 0:
self.spawnqueue = Queue()
self.spawn_evaluators()
while self.running.is_set():
self.log.exception(e)
self.terminate()
self.load_bumplimit_set()
if self.c.tcount == 0:
self.join_threads()
self.load_targets()
self.inter_sleep(5)
self.pc.check_waiting()
if self.c.tcount > 0:
self.load_users()
new = self.read_newproxies()
self.save_users()
self.spawn_wipethreads()
if not new:
self.save_targets()
self.inter_sleep(5)
self.add_spawns(new)
