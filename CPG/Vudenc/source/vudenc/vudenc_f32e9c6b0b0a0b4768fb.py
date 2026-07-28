@forbid_ui_on_replica...
ticket = self.decode_link_ticket()
success = True
error_msg = None
replication.become_replica(ticket, api.get_current_identity())
success = False
env = {'error_msg': error_msg, 'page_title': 'Switch', 'primary_id': ticket
    .primary_id, 'primary_url': ticket.primary_url, 'success': success}
error_msg = exc.message
self.reply('auth/admin/linking_done.html', env)
