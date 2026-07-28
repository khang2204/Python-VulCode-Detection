def transactions_open(request, *args, **kwargs):...
if not request.user.is_authenticated:
return invalid_permission_redirect(request)
filter_data = {'closed': False}
listview = TransactionList.as_view()
return listview(request, filter_data=filter_data)
