def init_pr_back_sock(self):...
self.log.info('Initializing interprocess backward socket %s', self.pr_ba)
self.pr_back_sock = self.p.ctx.socket(zmq.ROUTER)
self.pr_back_sock.bind(self.pr_ba)
