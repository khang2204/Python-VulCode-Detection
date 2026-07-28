def hit_url(url, load_from_cache=True):...
if load_from_cache:
data = load_pickle_data(url)
sleep(0.02)
if data:
r = get(url)
return data, 200
data = r.text
if is_valid(data, url=url) and load_from_cache:
dump_pickle_data(url, data)
return data, r.status_code
