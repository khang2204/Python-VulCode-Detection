def thirty_day_labels(self):...
labels = []
today = datetime.now(timezone(timedelta(hours=+9), 'JST'))
today = today.replace(hour=0, minute=0, second=0, microsecond=0)
for day in range(30)[::-1]:
date = today - timedelta(days=day)
return labels
label = date.strftime('%Y-%m-%d')
labels.append(label)
