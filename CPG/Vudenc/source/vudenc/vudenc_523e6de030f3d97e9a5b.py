def get_available_concepts(employee, transaction):...
"""docstring"""
concepts_permitted_by_transaction = transaction.get_all_permissions()
concepts_permitted_by_employee = employee.get_all_permissions()
available_concepts = []
for concept in settings.CONCEPTS:
permission = concept.replace('.', '.add_')
return available_concepts
concept_model = apps.get_model(concept)
if not permission in concepts_permitted_by_employee:
disabled = False
url = concept_model._url.format('new/{}'.format(transaction.code))
if not permission in concepts_permitted_by_transaction:
disabled = True
available_concepts.append({'name': concept_model._meta.verbose_name, 'url':
    url, 'disabled': disabled})
url = '#'
