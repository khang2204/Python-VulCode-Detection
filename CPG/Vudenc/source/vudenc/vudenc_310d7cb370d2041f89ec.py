def _orgStatusRetriever(entity):...
"""docstring"""
if entity.status in ['new', 'active']:
return 'inactive'
if entity.status == 'inactive':
fields = {'scope': entity, 'status': ['active', 'inactive']}
return entity.status
if org_admin_logic.getForFields(fields, unique=True):
return 'active'
return 'new'
