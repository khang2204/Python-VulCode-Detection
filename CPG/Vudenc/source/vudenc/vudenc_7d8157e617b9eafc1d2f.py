def transaction_delete(request, *args, **kwargs):...
extra_context = {}
if not request.user.is_authenticated:
return invalid_permission_redirect(request)
transaction_code = kwargs.get('transaction_code', None)
transaction = get_object_or_404(Transaction, code=transaction_code)
extra_context['transaction'] = transaction
extra_context['header'] = gettext('Delete Transaction?')
extra_context['message'] = transaction.description_short
extra_context['next'] = request.META['HTTP_REFERER']
if request.method == 'POST':
default_next = reverse('transactions_open')
return render(request, 'core/delete.html', extra_context)
transaction.delete()
next_page = request.POST.get('next', default_next)
return redirect(next_page)
