@api_view(['GET'])...
measures = utils.param_to_list(request.query_params.get('measure', None))
tags = utils.param_to_list(request.query_params.get('tags', None))
qs = MeasureGlobal.objects.select_related('measure')
if measures:
qs = qs.filter(measure_id__in=measures)
if tags:
qs = qs.filter(measure__tags__overlap=tags)
qs = qs.order_by('measure_id', 'month')
rolled = {}
for mg in qs:
id = mg.measure_id
d = {'measures': [rolled[k] for k in rolled]}
d_copy = {'date': mg.month, 'numerator': mg.numerator, 'denominator': mg.
    denominator, 'calc_value': mg.calc_value, 'percentiles': mg.percentiles,
    'cost_savings': mg.cost_savings}
return Response(d)
if id in rolled:
rolled[id]['data'].append(d_copy)
measure = mg.measure
if measure.tags_focus:
tags_focus = ','.join(measure.tags_focus)
tags_focus = ''
rolled[id] = {'id': id, 'name': measure.name, 'title': measure.title,
    'description': measure.description, 'why_it_matters': measure.
    why_it_matters, 'numerator_short': measure.numerator_short,
    'denominator_short': measure.denominator_short, 'url': measure.url,
    'is_cost_based': measure.is_cost_based, 'is_percentage': measure.
    is_percentage, 'low_is_good': measure.low_is_good, 'tags_focus':
    tags_focus, 'numerator_is_list_of_bnf_codes': measure.
    numerator_is_list_of_bnf_codes, 'tags': _hydrate_tags(measure.tags),
    'data': [d_copy]}
