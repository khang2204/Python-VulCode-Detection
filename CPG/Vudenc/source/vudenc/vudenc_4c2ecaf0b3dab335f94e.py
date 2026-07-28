def _create_conn(self):...
return Client(host=self.host, port=self.port, connect_timeout=self.
    connect_timeout, send_receive_timeout=self.send_receive_timeout,
    settings=self.client_settings)
