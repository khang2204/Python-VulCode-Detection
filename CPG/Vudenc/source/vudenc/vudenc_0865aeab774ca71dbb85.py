def thirty_day_data(self):...
data = []
today = datetime.now(timezone(timedelta(hours=+9), 'JST'))
today = today.replace(hour=0, minute=0, second=0, microsecond=0)
for day in range(30)[::-1]:
from_date = today - timedelta(days=day)
return data
to_date = today - timedelta(days=day - 1)
count = self.object_list.filter(timestamp__gte=from_date, timestamp__lte=
    to_date).count()
data.append(count)
