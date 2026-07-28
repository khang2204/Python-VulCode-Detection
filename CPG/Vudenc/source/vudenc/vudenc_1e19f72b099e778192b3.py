def lineSend(self, csessid, data):...
"""docstring"""
request = self.requests.get(csessid)
if request:
request.write(jsonify(data))
dataentries = self.databuffer.get(csessid, [])
request.finish()
dataentries.append(jsonify(data))
self.databuffer[csessid] = dataentries
