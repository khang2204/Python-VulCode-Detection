def mode_close(self, request):...
"""docstring"""
csessid = request.args.get('csessid')[0]
sess = self.sessionhandler.sessions_from_csessid(csessid)[0]
self.client_disconnect(csessid)
return '""'
sess.sessionhandler.disconnect(sess)
