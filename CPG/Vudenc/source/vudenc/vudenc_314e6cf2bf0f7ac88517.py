def _get_org_id_and_type_from_request(request):...
"""docstring"""
org_id = utils.param_to_list(request.query_params.get('org', []))
org_id = org_id and org_id[0]
org_type = None
if 'org_type' in request.query_params:
org_type = request.query_params['org_type'] + '_id'
if org_id:
if org_type in ['pct_id', 'ccg_id']:
if len(org_id) == 3:
return org_id, org_type
org_type = 'pr.ccg_id'
org_type = 'pr.ccg_id'
if len(org_id) == 6:
org_type = 'practice_id'
assert False, 'Unexpected org: {}'.format(org_id)
