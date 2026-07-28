@login_required()...
extra_context = {}
concept, concept_form = get_concept_and_form_from_kwargs(**kwargs)
extra_context['concept'] = concept
transaction = concept.transaction
extra_context['transaction'] = transaction
return render(request, 'transactions/concept_detail.html', extra_context)
