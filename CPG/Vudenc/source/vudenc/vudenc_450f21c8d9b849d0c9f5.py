def _processProgramFreezing(program_entity, mode):...
"""docstring"""
new_context = {}
new_context['new_status'] = 'active' if mode == 'unfreeze' else 'inactive'
old_status = 'inactive' if mode == 'unfreeze' else 'active'
new_context['fields'] = pickle.dumps({'scope': program_entity.key(),
    'status': old_status})
for pattern in ROLE_PER_SCOPE_MODELS_URL_PATTERNS:
responses.startTask(_constructRequestURL(pattern), context=new_context)
new_context['fields'] = pickle.dumps({'program': program_entity.key(),
    'status': old_status})
for pattern in ROLE_PER_PROGRAM_MODELS_URL_PATTERNS:
responses.startTask(_constructRequestURL(pattern), context=new_context)
new_context = {}
old_status = 'inactive' if mode == 'unfreeze' else ['active', 'new']
new_context['fields'] = pickle.dumps({'scope': program_entity.key(),
    'status': old_status})
responses.startTask(_constructRequestURL(ORG_MODEL_URL_PATTERNS[0]),
    context=new_context)
return
