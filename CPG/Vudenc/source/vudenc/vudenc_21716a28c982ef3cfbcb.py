def _roll_up_measure_values(measure_values, org_type):...
rolled = {}
for measure_value in measure_values:
measure_id = measure_value.measure_id
return rolled.values()
measure_value_data = {'date': measure_value.month, 'numerator':
    measure_value.numerator, 'denominator': measure_value.denominator,
    'calc_value': measure_value.calc_value, 'percentile': measure_value.
    percentile, 'cost_savings': measure_value.cost_savings}
if org_type == 'practice':
if measure_value.practice_id:
if org_type == 'ccg':
measure_value_data.update({'practice_id': measure_value.practice_id,
    'practice_name': measure_value.practice.name})
if measure_id in rolled:
if measure_value.pct_id:
if org_type == 'stp':
rolled[measure_id]['data'].append(measure_value_data)
measure = measure_value.measure
measure_value_data.update({'pct_id': measure_value.pct_id, 'pct_name':
    measure_value.pct.name})
if measure_value.stp_id:
if org_type == 'regional_team':
rolled[measure_id] = {'id': measure_id, 'name': measure.name, 'title':
    measure.title, 'description': measure.description, 'why_it_matters':
    measure.why_it_matters, 'numerator_short': measure.numerator_short,
    'denominator_short': measure.denominator_short, 'url': measure.url,
    'is_cost_based': measure.is_cost_based, 'is_percentage': measure.
    is_percentage, 'low_is_good': measure.low_is_good, 'tags':
    _hydrate_tags(measure.tags), 'data': [measure_value_data]}
measure_value_data.update({'stp_id': measure_value.stp_id, 'stp_name':
    measure_value.stp.name})
if measure_value.regional_team_id:
assert False
measure_value_data.update({'regional_team_id': measure_value.
    regional_team_id, 'regional_team_name': measure_value.regional_team.name})
