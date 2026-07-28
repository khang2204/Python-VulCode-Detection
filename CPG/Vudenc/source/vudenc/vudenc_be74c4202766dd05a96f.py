def post(self, request, *args, **kwargs):...
if not request.user.is_authenticated:
return invalid_permission_redirect(request)
print_transaction = request.POST.get('print_transaction', None)
if print_transaction:
transaction = get_object_or_404(Transaction, code=print_transaction)
request.method = 'GET'
resp = HttpResponse(content_type='application/pdf')
return self.get(request, *args, **kwargs)
resp['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(
    transaction.code)
context = {'transaction': transaction}
result = generate_pdf('transactions/invoice.html', file_object=resp,
    context=context)
return result
