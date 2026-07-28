def _make_flat_wins_csv(self, **kwargs):...
"""docstring"""
sql_str = 'SELECT id FROM wins_completed_wins_fy'
if self.end_date:
sql_str = f"{sql_str} where created <= '{self.end_date.strftime('%m-%d-%Y')}'"
cursor.execute(sql_str)
ids = cursor.fetchall()
wins = Win.objects.filter(id__in=[id[0] for id in ids]).values()
for win in wins:
yield self._get_win_data(win)
