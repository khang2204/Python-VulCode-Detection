def send_to_wm(frames):...
msg = [frames[0]]
msg.extend(wzrpc.make_sig_msg(frames[1], frames[2], frames[3:]))
sig_sock.send_multipart(msg)
