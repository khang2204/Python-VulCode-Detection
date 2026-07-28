def get_date(url):...
url = url + '/log'
bracket, status = hit_url(url)
s2 = '2015-03-07'
if 'created_at' not in bracket:
return s2
first_occurance = str(bracket).index('created_at')
bracket = bracket[first_occurance:]
s = 'created_at":"'
i = len(s)
i2 = len(s2) + i
date = bracket[i:i2]
y = date.split('-')[0]
m = date.split('-')[1]
d = date.split('-')[2]
return date
