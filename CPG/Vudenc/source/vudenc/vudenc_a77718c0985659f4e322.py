def get_epoch_day(self, date):...
s = date.split('-')
epoch_start = int(datetime(int(s[0]), int(s[1]), int(s[2]), 0, 0, 0, tzinfo
    =pytz.utc).timestamp())
epoch_end = int(datetime(int(s[0]), int(s[1]), int(s[2]), 23, 59, 59,
    tzinfo=pytz.utc).timestamp())
return epoch_start, epoch_end
