def terminate(self):...
msg = [b'GLOBAL']
msg.extend(wzrpc.make_sig_msg(b'WZWorker', b'terminate', []))
if hasattr(self, 'th_sock'):
self.th_sock.send_multipart(msg)
if hasattr(self, 'pr_sock'):
self.pr_sock.send_multipart(msg)
