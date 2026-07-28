def __exit__(self, exc_type, exc_val, exc_tb):...
if self.conn:
self.cur.close()
self.conn.close()
