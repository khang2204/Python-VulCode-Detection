def tid_num_to_tid(self, tid_num):...
"""docstring"""
q = "SELECT tid FROM tids WHERE rowid = '" + str(tid_num) + "'"
self.query(q)
return self.c.fetchone()[0]
