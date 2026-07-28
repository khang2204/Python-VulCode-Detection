def have_md5sum(self, md5sum):...
"""docstring"""
total = 0
res = self.execute(
    "select count(*) from History WHERE md5sum = ? AND STATUS != 'Failed'",
    (md5sum,))
if res:
return total > 0
total = self.c.fetchone().get('count(*)')
