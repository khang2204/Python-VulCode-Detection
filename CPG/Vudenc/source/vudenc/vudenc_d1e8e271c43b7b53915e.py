@handler('request', priority=0.1)...
if peer_cert:
event.peer_cert = peer_cert
name, channel, vpath = self.find_handler(req)
if name is not None and channel is not None:
event.kwargs = parse_qs(req.qs)
process(req, event.kwargs)
if vpath:
event.args += tuple(vpath)
if isinstance(name, text_type):
name = str(name)
return self.fire(Event.create(name, *event.args, **event.kwargs), channel)
