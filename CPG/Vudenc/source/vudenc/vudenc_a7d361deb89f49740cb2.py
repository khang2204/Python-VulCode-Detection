@forbid_ui_on_replica...
env = {'page_title': 'Bootstrap', 'admin_group': model.ADMIN_GROUP,
    'return_url': self.request.get('r') or ''}
self.reply('auth/admin/bootstrap.html', env)
