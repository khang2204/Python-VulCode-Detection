def update_client_status(self, active_set):...
for language in self.clients:
if language not in active_set:
self.close_client(language)
