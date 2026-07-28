def mode_init(self, request):...
"""docstring"""
csessid = request.args.get('csessid')[0]
remote_addr = request.getClientIP()
host_string = '%s (%s:%s)' % (_SERVERNAME, request.getRequestHostname(),
    request.getHost().port)
sess = AjaxWebClientSession()
sess.client = self
sess.init_session('ajax/comet', remote_addr, self.sessionhandler)
sess.csessid = csessid
csession = _CLIENT_SESSIONS(session_key=sess.csessid)
uid = csession and csession.get('webclient_authenticated_uid', False)
if uid:
sess.uid = uid
sess.sessionhandler.connect(sess)
sess.logged_in = True
self.last_alive[csessid] = time.time(), False
if not self.keep_alive:
self.keep_alive = LoopingCall(self._keepalive)
return jsonify({'msg': host_string, 'csessid': csessid})
self.keep_alive.start(_KEEPALIVE, now=False)
