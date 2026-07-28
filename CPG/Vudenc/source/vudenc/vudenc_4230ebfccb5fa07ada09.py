def __init__(self, redirection_source):...
self.active = False
self.bytes_buffer = io.BytesIO()
self.redirection_source = redirection_source
self.last_write_time = 0
super(RedirectBuffer, self).__init__(buffer=self.bytes_buffer, encoding=
    redirection_source.encoding, write_through=True)
