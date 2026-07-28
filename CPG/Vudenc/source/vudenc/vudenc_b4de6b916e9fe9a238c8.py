def update_server_list(self):...
for language in self.configurations_for_servers:
config = {'status': self.STOPPED, 'config': CONF.get('lsp-server', language
    ), 'instance': None}
if language not in self.clients:
self.clients[language] = config
logger.debug(self.clients[language]['config'] != config['config'])
self.register_queue[language] = []
current_config = self.clients[language]['config']
new_config = config['config']
restart_diff = ['cmd', 'args', 'host', 'port', 'external']
restart = any([(current_config[x] != new_config[x]) for x in restart_diff])
if restart:
if self.clients[language]['status'] == self.STOPPED:
if self.clients[language]['status'] == self.RUNNING:
self.clients[language] = config
if self.clients[language]['status'] == self.RUNNING:
client = self.clients[language]['instance']
self.close_client(language)
client.send_plugin_configurations(new_config['configurations'])
self.clients[language] = config
self.start_lsp_client(language)
