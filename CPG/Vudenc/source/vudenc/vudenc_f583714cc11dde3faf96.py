def send_output(self, output):...
if self.current.user_id is None or 'login_process' in output:
self.client_queue.send_to_default_exchange(self.sessid, output)
self.client_queue.send_to_prv_exchange(self.current.user_id, output)
