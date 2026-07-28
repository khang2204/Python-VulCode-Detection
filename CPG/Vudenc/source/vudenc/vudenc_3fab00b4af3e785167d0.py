def get_previous_month(date):...
y, m, d = date.split('-')
m = '12' if m == '01' else str(int(m) - 1).zfill(2)
y = str(int(y) - 1).zfill(2) if m == '12' else y
date = '{}-{}-{}'.format(y, m, d)
return date
