@require_GET...
"""docstring"""
objects = _InfoObjects(request=request, product_id=request.GET.get(
    'product_id'))
info_type = getattr(objects, request.GET.get('info_type'))
if not info_type:
return HttpResponse('Unrecognizable info-type')
if request.GET.get('format') == 'ulli':
field = request.GET.get('field', default='name')
return HttpResponse(serializers.serialize('json', info_type(), fields=(
    'name', 'value')))
response_str = '<ul>'
for obj_value in info_type().values(field):
response_str += '<li>' + obj_value.get(field, None) + '</li>'
response_str += '</ul>'
return HttpResponse(response_str)
