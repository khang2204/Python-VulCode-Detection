def send_keepalive(self):...
msg = self.p.wz.make_req_msg(b'Router', b'bind-keepalive', [], self.
    handle_keepalive_reply)
msg.insert(0, b'')
self.p.wz_sock.send_multipart(msg)
