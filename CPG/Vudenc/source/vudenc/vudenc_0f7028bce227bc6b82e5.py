def __call__(self, parent):...
self.p = parent
self.p.wz_connect()
self.p.wz_auth_requests = [(b'Router', b'auth-bind-route'), (b'Router',
    b'auth-unbind-route'), (b'Router', b'auth-set-route-type')]
self.p.wz_bind_methods = [(b'Evaluator', b'evaluate', self.handle_evaluate,
    wzrpc.routetype.random)]
self.p.auth_requests()
self.p.bind_methods()
self.ev = self.ev_init()
self.bind_kt_ticker.tick()
while self.p.running.is_set():
socks = self.p.poll()
if self.bind_kt_ticker.elapsed(False) > self.bind_kt:
self.bind_kt_ticker.tick()
self.send_keepalive()
