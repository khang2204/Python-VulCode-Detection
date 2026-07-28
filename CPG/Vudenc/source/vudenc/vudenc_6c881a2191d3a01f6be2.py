def get_last_day_of_month(self, date):...
day = datetime.strptime(date, '%Y-%m-%d')
next_month = day.replace(day=28) + timedelta(days=4)
return (next_month - timedelta(days=next_month.day)).day
