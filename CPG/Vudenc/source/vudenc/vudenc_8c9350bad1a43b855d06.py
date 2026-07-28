def _measure_by_org(request, org_type):...
measure_ids = utils.param_to_list(request.query_params.get('measure', None))
tags = utils.param_to_list(request.query_params.get('tags', []))
org_ids = utils.param_to_list(request.query_params.get('org', []))
parent_org_type = request.query_params.get('parent_org_type', None)
aggregate = bool(request.query_params.get('aggregate'))
if org_type == 'practice' and not (org_ids or aggregate):
if len(org_ids) > 1 and len(measure_ids) > 1:
if parent_org_type is None:
if org_type == 'practice' and org_ids:
measure_values = MeasureValue.objects.by_org(org_type, parent_org_type,
    org_ids, measure_ids, tags)
l = len(org_ids[0])
parent_org_type = org_type
org_field = org_type if org_type != 'ccg' else 'pct'
assert all(len(org_id) == l for org_id in org_ids)
measure_values = measure_values.prefetch_related(org_field)
if l == 3:
if aggregate:
parent_org_type = 'pct'
if l == 6:
measure_values = measure_values.aggregate_by_measure_and_month()
rsp_data = {'measures': _roll_up_measure_values(measure_values, org_type)}
parent_org_type = 'practice'
assert False, l
return Response(rsp_data)
