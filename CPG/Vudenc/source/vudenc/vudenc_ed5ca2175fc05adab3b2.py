def init_pr_sock(self):...
self.log.info('Initializing interprocess signal socket %s', self.pr_sa)
self.pr_sock = self.p.ctx.socket(zmq.PUB)
self.pr_sock.bind(self.pr_sa)
