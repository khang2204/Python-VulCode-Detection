def is_timestamps_from_same_day(self, ts1, ts2):...
d1 = datetime.fromtimestamp(ts1)
d2 = datetime.fromtimestamp(ts2)
return d1.year == d2.year and d1.month == d2.month and d1.day == d2.day
