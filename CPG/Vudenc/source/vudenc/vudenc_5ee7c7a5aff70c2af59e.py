@login_required()...
extra_context = {}
concept, concept_form = get_concept_and_form_from_kwargs(**kwargs)
extra_context['concept'] = concept
transaction = concept.transaction
if transaction.closed:
return redirect('message', message=gettext('Transaction Closed'))
extra_context['transaction'] = transaction
if request.method == 'POST':
form = concept_form(request.POST, instance=concept)
form = concept_form(instance=concept)
if form.is_valid():
extra_context['form'] = form
form.save()
extra_context['form'] = form
return render(request, 'transactions/concept_edit.html', extra_context)
return redirect('transaction_edit', transaction_code=transaction.code)
return render(request, 'transactions/concept_edit.html', extra_context)
