@forbid_ui_on_replica...
added = model.bootstrap_group(model.ADMIN_GROUP, [api.get_current_identity(
    )], 'Users that can manage groups')
env = {'page_title': 'Bootstrap', 'admin_group': model.ADMIN_GROUP, 'added':
    added, 'return_url': self.request.get('return_url') or ''}
self.reply('auth/admin/bootstrap_done.html', env)
