def parse_date(date_):...
if date_ is None:
return
masks = ['%Y-%m-%d', '%Y-%m-%dT%H:%M', '%Y-%m-%d %H:%M']
for mask in masks:
return datetime.strptime(date_, mask)
