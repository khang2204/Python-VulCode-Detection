def decode_link_ticket(self):...
"""docstring"""
return replication.decode_link_ticket(self.request.get('t').encode('ascii'))
self.abort(400)
return
