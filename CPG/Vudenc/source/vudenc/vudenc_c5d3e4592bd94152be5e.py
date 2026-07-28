@login_required...
extra_context = {}
if not request.user.is_authenticated:
return invalid_permission_redirect(request)
transaction_code = kwargs.get('transaction_code', None)
transaction = get_object_or_404(Transaction, code=transaction_code)
extra_context['transaction'] = transaction
return render(request, 'transactions/transaction_detail.html', extra_context)
