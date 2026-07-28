def _make_flat_wins_csv(self, deleted=False):...
"""docstring"""
if deleted:
wins = Win.objects.inactive()
wins = Win.objects.all()
if deleted:
wins = wins.exclude(user__email__in=settings.IGNORE_USERS)
wins = wins.values()
win_datas = [self._get_win_data(win) for win in wins]
stringio = io.StringIO()
stringio.write(u'\ufeff')
if win_datas:
csv_writer = csv.DictWriter(stringio, win_datas[0].keys())
return stringio.getvalue()
csv_writer.writeheader()
for win_data in win_datas:
csv_writer.writerow(win_data)
