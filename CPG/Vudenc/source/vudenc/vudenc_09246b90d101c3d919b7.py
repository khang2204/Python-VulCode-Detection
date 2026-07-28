def at_login(self):...
csession = self.get_client_session()
if csession:
csession['webclient_authenticated_uid'] = self.uid
csession.save()
