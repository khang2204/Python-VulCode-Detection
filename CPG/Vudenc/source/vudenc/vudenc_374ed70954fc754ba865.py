def open(self):...
if not login_get_current_user(self):
return None
runScriptWebSocketConnections.add(self)
