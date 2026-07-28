import zmq
import threading, multiprocessing
import logging
from sup.ticker import Ticker
import wzrpc
from wzrpc.wzhandler import WZHandler
import wzauth_data
"""Exception to raise when self.running is cleared"""
def __init__(self):...
super().__init__('Worker was interrupted at runtime')
"""Exception to raise on suspend signal"""
def __init__(self, interval, *args, **kvargs):...
self.interval = interval
super().__init__(*args, **kvargs)
"""Exception to raise when suspend sleep is interrupted"""
def __init__(self, wz_addr, fun, args=(), kvargs={}, name=None, start_timer...
super().__init__(*pargs, **pkvargs)
self.name = name if name else type(self).__name__
self.start_timer = start_timer
self.poll_timeout = poll_timeout if poll_timeout else 5 * 1000
self.call = fun, args, kvargs
self.wz_addr = wz_addr
self.wz_auth_requests = []
self.wz_bind_methods = []
self.wz_poll_timeout = 30
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
def wz_connect(self):...
self.wz_sock.connect(self.wz_addr)
def wz_wait_reply(self, fun, interface, method, data, reqid=None, timeout=None...
s, p, t, wz = self.wz_sock, self.poll, self.sleep_ticker, self.wz
timeout = timeout if timeout else self.wz_poll_timeout
rs = wzrpc.RequestState(fun)
msg = self.wz.make_req_msg(interface, method, data, rs.accept, reqid)
msg.insert(0, b'')
s.send_multipart(msg)
t.tick()
while self.running.is_set():
p(timeout * 1000)
def wz_multiwait(self, requests):...
if rs.finished:
s, p, t, wz = self.wz_sock, self.poll, self.sleep_ticker, self.wz
if rs.retry:
elapsed = t.elapsed(False)
timeout = self.wz_poll_timeout
msg = self.wz.make_req_msg(interface, method, data, rs.accept, reqid)
return
if elapsed >= timeout:
rslist = []
msg.insert(0, b'')
t.tick()
msgdict = {}
s.send_multipart(msg)
rs.accept(None, 0, 255, [elapsed])
for request in requests:
rs.finished = False
rs = wzrpc.RequestState(request[0])
while self.running.is_set():
rs.retry = False
rslist.append(rs)
flag = 0
def auth_requests(self):...
msg = self.wz.make_req_msg(request[1][0], request[1][1], request[1][2], rs.
    accept, request[1][3])
for rs in rslist:
for i, m in self.wz_auth_requests:
msg.insert(0, b'')
if rs.finished:
if not flag:
def accept(that, reqid, seqnum, status, data):...
def bind_route(self, i, m, f):...
msgdict[rs] = msg
if not rs.retry:
flag = 1
return
t.tick()
if status == wzrpc.status.success:
self.log.debug('Binding %s,%s route', i, m)
s.send_multipart(msg)
s.send_multipart(msgdict[rs])
p(timeout * 1000)
self.log.debug('Successfull auth for (%s, %s)', i, m)
if status == wzrpc.status.e_auth_wrong_hash:
def accept(that, reqid, seqnum, status, data):...
rs.finished = False
if t.elapsed(False) >= timeout:
self.wz_wait_reply(accept, *self.wz.make_auth_req_data(i, m, wzauth_data.
    request[i, m]))
if wzrpc.status.e_timeout:
if status == wzrpc.status.success:
rs.retry = False
for rs in rslist:
self.log.warn('Timeout {0}, retrying'.format(data[0]))
self.log.warning('Recvd unknown reply for (%s, %s) %s: %s', i, m, wzrpc.
    name_status(status), repr(data))
self.wz.set_req_handler(i, m, f)
if status == wzrpc.status.e_req_denied:
if not rs.finished:
that.retry = True
self.log.debug('Succesfully binded route (%s, %s)', i, m)
self.log.warn('Status {0}, reauthentificating'.format(wzrpc.name_status(
    status)))
if wzrpc.status.e_timeout:
rs.accept(None, 0, 255, [])
return self.wz_wait_reply(accept, *self.wz.make_auth_bind_route_data(i, m,
    wzauth_data.bind_route[i, m]))
self.auth_requests()
self.log.warn('Timeout {0}, retrying'.format(data[0]))
self.log.warn('Status {0}, retrying'.format(wzrpc.name_status(status)))
rs.finished = True
that.retry = True
that.retry = True
