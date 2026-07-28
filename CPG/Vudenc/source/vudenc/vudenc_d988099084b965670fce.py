def has_month_passed(date):...
y, m, d = date.split('-')
today = datetime.datetime.today().strftime('%Y-%m-%d')
today_y, today_m, today_d = today.split('-')
if m == today_m:
return False
if today_d == '01':
return True
return False
