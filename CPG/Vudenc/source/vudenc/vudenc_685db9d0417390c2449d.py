@forbid_ui_on_replica...
ticket = self.decode_link_ticket()
env = {'generated_by': ticket.generated_by, 'page_title': 'Switch',
    'primary_id': ticket.primary_id, 'primary_url': ticket.primary_url}
self.reply('auth/admin/linking.html', env)
