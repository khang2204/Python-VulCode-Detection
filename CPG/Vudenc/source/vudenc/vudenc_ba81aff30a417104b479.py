def send_request(self, language, request, params):...
if language in self.clients:
language_client = self.clients[language]
if language_client['status'] == self.RUNNING:
client = self.clients[language]['instance']
client.perform_request(request, params)
