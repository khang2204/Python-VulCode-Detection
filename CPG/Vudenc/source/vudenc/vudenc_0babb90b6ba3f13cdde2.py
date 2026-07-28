def init_th_back_sock(self):...
self.log.info('Initializing intraprocess backward socket %s', self.th_ba)
self.th_back_sock = self.p.ctx.socket(zmq.ROUTER)
self.th_back_sock.bind(self.th_ba)
