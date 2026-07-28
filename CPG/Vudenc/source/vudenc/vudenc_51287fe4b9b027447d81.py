def show_page(self, web_client_id, saved=False):...
env = {'page_title': 'OAuth2 web client ID', 'web_client_id': web_client_id or
    '', 'saved': saved}
self.reply('auth/admin/bootstrap_oauth.html', env)
