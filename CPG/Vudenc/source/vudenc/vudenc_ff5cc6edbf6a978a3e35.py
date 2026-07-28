def get_valid_url_range(base_url):...
start_end = load_pickle_data(base_url)
if start_end:
start, end = start_end
start = _get_first_valid_url(base_url)
end = _get_last_valid_url(base_url, end)
end = _get_last_valid_url(base_url, start)
dump_pickle_data(base_url, (start, end))
return start, end
