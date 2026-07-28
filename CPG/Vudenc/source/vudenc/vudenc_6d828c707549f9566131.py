def _make_flat_wins_csv(self, deleted=False):...
"""docstring"""
if deleted:
wins = Win.objects.inactive()
wins = Win.objects.all()
if deleted:
wins = wins.exclude(user__email__in=settings.IGNORE_USERS)
wins = wins.values()
for win in wins:
yield self._get_win_data(win)
