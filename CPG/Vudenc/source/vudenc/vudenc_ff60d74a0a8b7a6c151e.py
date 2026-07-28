def get_script_log(self, nzo_id):...
"""docstring"""
data = ''
t = nzo_id,
if self.execute('SELECT script_log FROM history WHERE nzo_id=?', t):
return data
data = zlib.decompress(self.c.fetchone().get('script_log'))
