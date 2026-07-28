def _cmd_restart(self, message):...
logging.info('Rebooting bot: %s', message)
out = {'cmd': 'restart', 'message': message}
self.send_response(out)
