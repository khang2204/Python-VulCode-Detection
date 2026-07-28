def get_epoch_month(self, date):...
s = date.split('-')
epoch_start = int(datetime(int(s[0]), int(s[1]), 1, 0, 0, 0, tzinfo=pytz.
    utc).timestamp())
epoch_end = int(datetime(int(s[0]), int(s[1]), self.get_last_day_of_month(
    date), 23, 59, 59, tzinfo=pytz.utc).timestamp())
return epoch_start, epoch_end
