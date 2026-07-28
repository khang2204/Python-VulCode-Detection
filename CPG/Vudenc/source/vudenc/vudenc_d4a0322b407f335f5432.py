def get_date_range(dates):...
if dates:
return {'startDate': min(dates).strftime('%Y-%m-%d %H:%M'), 'endDate': max(
    dates).strftime('%Y-%m-%d %H:%M')}
