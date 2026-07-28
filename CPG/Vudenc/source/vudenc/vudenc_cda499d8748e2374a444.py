def disconnect(self, reason='Server disconnected.'):...
"""docstring"""
csession = self.get_client_session()
if csession:
csession['webclient_authenticated_uid'] = None
self.client.lineSend(self.csessid, ['connection_close', [reason], {}])
csession.save()
self.client.client_disconnect(self.csessid)
self.logged_in = False
self.sessionhandler.disconnect(self)
