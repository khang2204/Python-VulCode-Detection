def iter_months(first, last, include_first=True, include_last=False):...
y, m, d = first.split('-')
last_y, last_m, last_d = last.split('-')
cur = '{}-{}'.format(y, m)
last = '{}-{}'.format(last_y, last_m)
months = []
if include_first:
months.append('{}-01'.format(cur))
op = operator.ge if include_last else operator.gt
while op(last, cur):
m = str(int(m) + 1)
return months[:len(months) - 1]
if m == '13':
m = '01'
m = m.zfill(2)
y = str(int(y) + 1)
cur = '{}-{}'.format(y, m)
months.append('{}-01'.format(cur))
