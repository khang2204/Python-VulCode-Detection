def _get_last_valid_url(base_url, start=1):...
invalid_count = 0
end = start
while invalid_count <= 30:
url = base_url.replace('###', str(start))
return end
print('about to check url {}'.format(url))
if debug:
print('start is ' + str(start))
data, status = hit_url(url)
if status < 300 and is_valid(data, url=base_url):
if debug:
invalid_count = invalid_count + 1
print('url ' + str(url) + ' is valid')
invalid_count = 0
start = start + 1
end = start
