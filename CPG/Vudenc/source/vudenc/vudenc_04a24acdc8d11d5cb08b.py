def have_episode(self, series, season, episode):...
"""docstring"""
total = 0
series = series.lower().replace('.', ' ').replace('_', ' ').replace('  ', ' ')
if series and season and episode:
pattern = '%s/%s/%s' % (series, season, episode)
return total > 0
res = self.execute(
    "select count(*) from History WHERE series = ? AND STATUS != 'Failed'",
    (pattern,))
if res:
total = self.c.fetchone().get('count(*)')
