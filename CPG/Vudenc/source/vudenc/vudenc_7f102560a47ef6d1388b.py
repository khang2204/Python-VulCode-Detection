def get_filter_args(filters):...
filters.clear_filters()
for arg in request.args:
re_match = re.findall('_flt_(\\d)_(.*)', arg)
if re_match:
filters.add_filter_index(re_match[0][1], int(re_match[0][0]), request.args.
    get(arg))
