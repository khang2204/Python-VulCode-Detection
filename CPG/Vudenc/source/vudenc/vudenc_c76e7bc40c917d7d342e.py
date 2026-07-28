def tid_to_tid_num(self, tid):...
"""docstring"""
q = "SELECT rowid FROM tids WHERE tid = '" + tid + "'"
self.query(q)
return self.c.fetchone()[0]
