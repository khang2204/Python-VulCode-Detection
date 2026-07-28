def get_history_size(self):...
"""docstring"""
total = 0
if self.execute('SELECT sum(bytes) FROM history'):
month_timest = int(this_month(time.time()))
total = self.c.fetchone().get('sum(bytes)')
month = 0
if self.execute('SELECT sum(bytes) FROM history WHERE "completed">?', (
week_timest = int(this_week(time.time()))
month = self.c.fetchone().get('sum(bytes)')
week = 0
if self.execute('SELECT sum(bytes) FROM history WHERE "completed">?', (
return total, month, week
week = self.c.fetchone().get('sum(bytes)')
