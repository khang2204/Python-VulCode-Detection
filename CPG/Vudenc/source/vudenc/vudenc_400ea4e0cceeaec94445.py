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
if rs.finished:
if rs.retry:
elapsed = t.elapsed(False)
msg = self.wz.make_req_msg(interface, method, data, rs.accept, reqid)
return
if elapsed >= timeout:
msg.insert(0, b'')
t.tick()
s.send_multipart(msg)
rs.accept(None, 0, 255, [elapsed])
rs.finished = False
rs.retry = False
