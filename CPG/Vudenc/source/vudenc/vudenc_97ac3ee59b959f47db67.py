def __init__(self, conn):...
self.conn = conn
self.s = conn.s
self.addr = conn.addr
self.args = conn.args
self.auth = conn.auth
self.sr = conn.sr
self.bufsz = 1024 * 32
self.ok = True
self.log_func = conn.log_func
self.log_src = conn.log_src
