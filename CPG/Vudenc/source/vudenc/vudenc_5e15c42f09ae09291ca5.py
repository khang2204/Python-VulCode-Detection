def get_name(self, nzo_id):...
"""docstring"""
t = nzo_id,
name = ''
if self.execute('SELECT name FROM history WHERE nzo_id=?', t):
return name
name = self.c.fetchone().get('name')
