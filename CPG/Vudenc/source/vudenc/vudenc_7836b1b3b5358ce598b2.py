@property...
session_id = None
session_id = self.request.headers.get('X-Session')
if session_id is None:
session_id = self.get_argument('x-session', default=None)
if session_id is None:
return None
session = GLSetting.sessions[session_id]
return None
return session
