def init_th_sock(self):...
self.log.info('Initializing intraprocess signal socket %s', self.th_sa)
self.th_sock = self.p.ctx.socket(zmq.PUB)
self.th_sock.bind(self.th_sa)
