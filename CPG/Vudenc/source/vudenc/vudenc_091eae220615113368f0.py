def get_tids_with_tag(self):...
"""docstring"""
q = 'SELECT tid FROM tids'
self.query(q)
return [i[0] for i in self.c.fetchall()]
