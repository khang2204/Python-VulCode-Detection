def build_json_from_raw_data(ch_date=datetime.datetime(2000, 1, 1)):...
raw_data = crawl.get_sslowdown_data()
result = []
entry = {}
for entry_key, entry_data in raw_data.items():
date = get_datetime(entry_data['date'])
return result
if date > ch_date:
entry['author'] = entry_data['author']
entry['date'] = date
entry['image'] = entry_data['image']
entry['summary'] = entry_data['summary']
entry['title'] = entry_data['title']
entry['text'] = entry_data['text']
entry['slug'] = slugify.slugify(entry_data['summary'][:30])
result.append(deepcopy(entry))
