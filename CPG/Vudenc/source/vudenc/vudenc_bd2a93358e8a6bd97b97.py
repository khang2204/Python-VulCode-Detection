def generate_paginator(obj, request, items_per_page=ITEMS_PER_PAGE):...
"""docstring"""
page_num = page_list_id(request)
paginator = {}
paginator['page_count'] = obj.count()
paginator['max_pages'] = int(paginator['page_count'] / items_per_page + (
    paginator['page_count'] % items_per_page > 0))
if page_num > paginator['max_pages']:
page_num = paginator['max_pages']
paginator['next_page'] = page_num + 1 if page_num < paginator['max_pages'
    ] else paginator['max_pages']
paginator['prev_page'] = page_num - 1 if page_num > 1 else 1
paginator['first_item'] = page_num * items_per_page - (items_per_page - 1)
paginator['last_item'] = paginator['page_count'
    ] if page_num * items_per_page > paginator['page_count'
    ] else page_num * items_per_page
paginator['page_num'] = page_num
paginator['items_per_page'] = items_per_page
obj_list = obj.paginate(page_num, ITEMS_PER_PAGE)
return paginator, obj_list
