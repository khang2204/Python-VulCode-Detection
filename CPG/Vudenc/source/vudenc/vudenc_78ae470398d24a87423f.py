def start_lsp_client(self, language):...
started = False
if language in self.clients:
language_client = self.clients[language]
return started
queue = self.register_queue[language]
if os.environ.get('CI', False) and not os.environ.get(
return started
started = language_client['status'] == self.RUNNING
if language_client['status'] == self.STOPPED:
config = language_client['config']
if not config['external']:
port = select_port(default_port=config['port'])
language_client['instance'] = LSPClient(parent=self, server_settings=config,
    folder=self.get_root_path(), language=language)
config['port'] = port
for plugin in self.lsp_plugins:
language_client['instance'].register_plugin_type(plugin, self.lsp_plugins[
    plugin])
logger.info('Starting LSP client for {}...'.format(language))
language_client['instance'].start()
language_client['status'] = self.RUNNING
for entry in queue:
language_client.register_file(*entry)
self.register_queue[language] = []
