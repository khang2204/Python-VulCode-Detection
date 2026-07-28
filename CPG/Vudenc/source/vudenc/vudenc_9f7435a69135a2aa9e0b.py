@login_required()...
extra_context = {}
concept, concept_form = get_concept_and_form_from_kwargs(**kwargs)
extra_context['concept'] = concept
transaction = concept.transaction
if transaction.closed:
return redirect('message', message=gettext('Transaction Closed'))
extra_context['transaction'] = transaction
extra_context['header'] = gettext('Delete {}?'.format(concept.concept_type))
extra_context['message'] = concept.description_short
extra_context['next'] = request.META['HTTP_REFERER']
if request.method == 'POST':
default_next = reverse('transaction_detail', kwargs={'transaction_code':
    concept.transaction.code})
return render(request, 'core/delete.html', extra_context)
concept.delete()
next_page = request.POST.get('next', default_next)
return redirect(next_page)
