def get_page_args():...
"""docstring"""
pages = {}
for arg in request.args:
re_match = re.findall('page_(.*)', arg)
return pages
if re_match:
pages[re_match[0]] = int(request.args.get(arg))
