def _get_signature(self, timestamp):...
"""docstring"""
ha = hmac.new(b'd1b964811afb40118a12068ff74a12f4', digestmod=hashlib.sha1)
grant_type = self.login_data['grant_type']
client_id = self.login_data['client_id']
source = self.login_data['source']
ha.update(bytes(grant_type + client_id + source + timestamp, 'utf-8'))
return ha.hexdigest()
