def __sinit__(self):...
"""docstring"""
self.log = logging.getLogger(self.name)
self.running = threading.Event()
self.sleep_ticker = Ticker()
self.poller = zmq.Poller()
s = self.ctx.socket(zmq.SUB)
self.poller.register(s, zmq.POLLIN)
s.setsockopt(zmq.IPV6, True)
s.connect(self.sig_addr)
s.setsockopt(zmq.SUBSCRIBE, b'GLOBAL')
s.setsockopt(zmq.SUBSCRIBE, b'WZWorker')
s.setsockopt(zmq.SUBSCRIBE, bytes(self.name, 'utf-8'))
self.sig_sock = s
s = self.ctx.socket(zmq.DEALER)
self.poller.register(s, zmq.POLLIN)
s.setsockopt(zmq.IPV6, True)
self.wz_sock = s
self.wz = WZHandler()
def term_handler(interface, method, data):...
self.log.info('Termination signal %s recieved', repr((interface, method, data))
    )
self.term()
self.wz.set_sig_handler(b'WZWorker', b'terminate', term_handler)
def resumehandler(interface, method, data):...
self.log.info('Resume signal %s recieved', repr((interface, method, data)))
self.wz.set_sig_handler(b'WZWorker', b'resume', term_handler)
self.running.set()
