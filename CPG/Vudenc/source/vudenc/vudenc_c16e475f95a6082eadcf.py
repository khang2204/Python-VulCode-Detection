@login_required...
extra_context = {}
if not request.user.is_authenticated:
return invalid_permission_redirect(request)
transaction_code = kwargs.get('transaction_code', None)
if not transaction_code:
transaction = Transaction.objects.create(employee=request.user)
transaction = get_object_or_404(Transaction, code=transaction_code)
return redirect('transaction_edit', transaction_code=transaction.code)
extra_context['transaction'] = transaction
if transaction.closed:
return redirect('message', message=gettext('Transaction Closed'))
available_concepts = get_available_concepts(request.user, transaction)
extra_context['available_concepts'] = available_concepts
if request.method == 'POST':
form = TransactionEditForm(request.POST, instance=transaction)
form = TransactionEditForm(instance=transaction)
valid = form.is_valid()
extra_context['form'] = form
if form.data['cancel_button'] == 'True':
return render(request, 'transactions/transaction_edit.html', extra_context)
transaction.delete()
if valid:
return redirect('index')
transaction.save()
extra_context['form'] = form
if form.cleaned_data['save_button']:
return render(request, 'transactions/transaction_edit.html', extra_context)
return redirect('transaction_detail', transaction_code=transaction.code)
return redirect('transaction_pay', transaction_code=transaction.code)
