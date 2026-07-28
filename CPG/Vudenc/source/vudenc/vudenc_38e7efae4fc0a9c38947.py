def send_passthrough(frames):...
msg = [b'WipeManager']
msg.extend(wzrpc.make_sig_msg(b'WipeManager', b'passthrough', frames))
sig_sock.send_multipart(msg)
