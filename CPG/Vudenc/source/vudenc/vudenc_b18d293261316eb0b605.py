def get_path(self, nzo_id):...
"""docstring"""
t = nzo_id,
path = ''
if self.execute('SELECT path FROM history WHERE nzo_id=?', t):
return path
path = self.c.fetchone().get('path')
