def _handle_ping_pong(self, data, session):...
still_alive = KeepAlive(sess_id=session.sess_id).update_or_expire_session()
msg = {'msg': 'pong'}
if not still_alive:
msg.update(LOGIN_REQUIRED_MESSAGE)
return msg
