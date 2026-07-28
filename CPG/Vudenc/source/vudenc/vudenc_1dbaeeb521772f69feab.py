def get_page_size_args():...
"""docstring"""
page_sizes = {}
for arg in request.args:
re_match = re.findall('psize_(.*)', arg)
return page_sizes
if re_match:
page_sizes[re_match[0]] = int(request.args.get(arg))
