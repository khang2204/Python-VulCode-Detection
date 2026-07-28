@login_required...
extra_context = {}
if not request.user.is_authenticated:
return invalid_permission_redirect(request)
transaction_code = kwargs.get('transaction_code', None)
transaction = get_object_or_404(Transaction, code=transaction_code)
extra_context['transaction'] = transaction
if transaction.closed:
return redirect('message', message=gettext('Transaction Closed'))
if request.method == 'POST':
form = TransactionPayForm(request.POST, instance=transaction)
form = TransactionPayForm(instance=transaction)
valid = form.is_valid()
extra_context['form'] = form
if form.data['cancel_button'] == 'True':
return render(request, 'transactions/transaction_pay.html', extra_context)
transaction.delete()
if valid:
return redirect('index')
if form.cleaned_data['confirm_button']:
extra_context['form'] = form
transaction.closed = True
if form.cleaned_data['save_button']:
return render(request, 'transactions/transaction_pay.html', extra_context)
transaction.closed_date = timezone.datetime.now()
transaction.save()
transaction.save()
return redirect('transaction_detail', transaction_code=transaction.code)
return redirect('transaction_detail', transaction_code=transaction.code)
