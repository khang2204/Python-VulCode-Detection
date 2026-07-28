def register_file(self, language, filename, signal):...
if language in self.clients:
language_client = self.clients[language]['instance']
if language_client is None:
self.register_queue[language].append((filename, signal))
language_client.register_file(filename, signal)
