def mode_keepalive(self, request):...
"""docstring"""
csessid = request.args.get('csessid')[0]
self.last_alive[csessid] = time.time(), False
return '""'
