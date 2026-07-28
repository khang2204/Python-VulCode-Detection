@api_view(['GET'])...
measure = request.query_params.get('measure', None)
org_id, org_type = _get_org_id_and_type_from_request(request)
this_month = ImportLog.objects.latest_in_category('prescribing').current_at
three_months_ago = (this_month - relativedelta(months=2)).strftime('%Y-%m-01')
m = Measure.objects.get(pk=measure)
if m.numerator_is_list_of_bnf_codes:
if org_type in ['stp_id', 'regional_team_id']:
data = []
extra_join = """
            INNER JOIN frontend_practice pr
            ON p.practice_id = pr.code
            INNER JOIN frontend_pct
            ON frontend_pct.code = pr.ccg_id
            """
if org_type == 'pr.ccg_id':
response = Response(data)
match = re.match('SUM\\((items|quantity|actual_cost)\\) AS numerator', m.
    numerator_columns)
extra_join = """
            INNER JOIN frontend_practice pr
            ON p.practice_id = pr.code
            """
extra_join = ''
filename = '%s-%s-breakdown.csv' % (measure, org_id)
if match:
if request.accepted_renderer.format == 'csv':
order_col = {'items': 'total_items', 'actual_cost': 'cost', 'quantity':
    'quantity'}[match.groups()[0]]
order_col = 'total_items'
response['content-disposition'] = 'attachment; filename=%s' % filename
return response
focus_on_org = org_id and org_type
params = {'numerator_bnf_codes': m.numerator_bnf_codes, 'three_months_ago':
    three_months_ago}
if focus_on_org:
org_condition = '{org_type} = %(org_id)s AND '.format(org_type=org_type)
org_condition = ''
org_group = '{org_type}, '.format(org_type=org_type)
org_group = ''
params['org_id'] = org_id
query = (
    """
            SELECT
              presentation_code AS bnf_code,
              pn.name AS presentation_name,
              SUM(total_items) AS total_items,
              SUM(actual_cost) AS cost,
              SUM(quantity) AS quantity
            FROM
              frontend_prescription p
            INNER JOIN
              frontend_presentation pn
            ON p.presentation_code = pn.bnf_code
            {extra_join}
            WHERE
              {org_condition}
              processing_date >= %(three_months_ago)s
              AND
              pn.bnf_code = ANY(%(numerator_bnf_codes)s)
            GROUP BY
              {org_group}
              presentation_code, pn.name
            ORDER BY {order_col} DESC
            LIMIT 50
        """
    .format(org_condition=org_condition, org_group=org_group, org_type=
    org_type, three_months_ago=three_months_ago, extra_join=extra_join,
    order_col=order_col))
data = utils.execute_query(query, params)
