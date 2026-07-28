def get_other(self, nzo_id):...
"""docstring"""
t = nzo_id,
if self.execute('SELECT * FROM history WHERE nzo_id=?', t):
return dtype, url, pp, script, cat
items = self.c.fetchall()[0]
return '', '', '', '', ''
dtype = items.get('report')
url = items.get('url')
pp = items.get('pp')
script = items.get('script')
cat = items.get('category')
