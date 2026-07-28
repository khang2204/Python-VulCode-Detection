def _get_first_valid_url(base_url):...
valid = False
index = 1
while not valid:
url = base_url.replace('###', str(index))
return index
data, status = hit_url(url)
if status < 300 and is_valid(data, url=base_url):
if debug:
if debug:
print('url ' + url + ' is valid')
valid = True
print('url ' + url + ' is not valid')
index = index + 1
