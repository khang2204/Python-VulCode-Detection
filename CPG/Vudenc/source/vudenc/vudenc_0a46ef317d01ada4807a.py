@api.onchange('date_begin')...
start_date = self.date_begin_located
if start_date:
self.fit_day_of_week = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S'
    ).strftime('%a')
