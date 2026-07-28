def get_prod_related_obj_json(request):...
"""docstring"""
data = request.GET.copy()
target = data.get('target', None)
p_pks = data.get('p_ids', None)
sep = data.get('sep', None)
if target and p_pks and sep:
p_pks = [k for k in p_pks.split(sep) if k]
res = []
res = get_prod_related_objs(p_pks, target)
return HttpResponse(json.dumps(res))
