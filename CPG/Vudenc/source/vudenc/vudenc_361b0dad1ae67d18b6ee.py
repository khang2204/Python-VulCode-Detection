def wz_multiwait(self, requests):...
s, p, t, wz = self.wz_sock, self.poll, self.sleep_ticker, self.wz
timeout = self.wz_poll_timeout
rslist = []
msgdict = {}
for request in requests:
rs = wzrpc.RequestState(request[0])
while self.running.is_set():
rslist.append(rs)
flag = 0
msg = self.wz.make_req_msg(request[1][0], request[1][1], request[1][2], rs.
    accept, request[1][3])
for rs in rslist:
msg.insert(0, b'')
if rs.finished:
if not flag:
msgdict[rs] = msg
if not rs.retry:
flag = 1
return
t.tick()
s.send_multipart(msg)
s.send_multipart(msgdict[rs])
p(timeout * 1000)
rs.finished = False
if t.elapsed(False) >= timeout:
rs.retry = False
for rs in rslist:
if not rs.finished:
rs.accept(None, 0, 255, [])
rs.finished = True
