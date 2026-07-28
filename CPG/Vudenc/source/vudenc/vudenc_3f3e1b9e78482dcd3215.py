def shutdown(self):...
logger.info('Shutting down LSP manager...')
for language in self.clients:
self.close_client(language)
