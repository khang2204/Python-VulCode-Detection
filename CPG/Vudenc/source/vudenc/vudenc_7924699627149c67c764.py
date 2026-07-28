def get_concept_and_form_from_kwargs(**kwargs):...
concept_form = kwargs.get('concept_form', None)
concept_class = concept_form._meta.model
transaction_code = kwargs.get('transaction_code', None)
if transaction_code:
transaction = get_transaction_from_kwargs(**kwargs)
concept_code = kwargs.get('concept_code', None)
return concept_class(transaction=transaction), concept_form
concept = get_object_or_404(concept_class, code=concept_code)
return concept, concept_form
