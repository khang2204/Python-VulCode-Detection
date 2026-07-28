def close_client(self, language):...
if language in self.clients:
language_client = self.clients[language]
if language_client['status'] == self.RUNNING:
logger.info('Stopping LSP client for {}...'.format(language))
language_client['status'] = self.STOPPED
language_client['instance'].stop()
