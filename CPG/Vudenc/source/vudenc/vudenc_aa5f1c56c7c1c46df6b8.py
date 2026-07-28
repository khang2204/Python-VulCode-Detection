def mode_receive(self, request):...
"""docstring"""
csessid = request.args.get('csessid')[0]
self.last_alive[csessid] = time.time(), False
dataentries = self.databuffer.get(csessid, [])
if dataentries:
return dataentries.pop(0)
request.notifyFinish().addErrback(self._responseFailed, csessid, request)
if csessid in self.requests:
self.requests[csessid].finish()
self.requests[csessid] = request
return server.NOT_DONE_YET
