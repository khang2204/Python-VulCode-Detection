def page_list_id(request):...
if not request.query.page:
return 1
page = int(request.query.page)
return 1
return page
