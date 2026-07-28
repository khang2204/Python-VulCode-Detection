def clean_date_params(query_dict, delta=7):...
"""docstring"""
now = datetime.now()
start_date_param = query_dict.get('startDate') or query_dict.get('startdate')
end_date_param = query_dict.get('endDate') or query_dict.get('enddate')
end_date = parse_date(end_date_param) or now
start_date = parse_date(start_date_param) or end_date - timedelta(days=delta)
if start_date > now or start_date.date() >= end_date.date():
start_date = now - timedelta(days=7)
return start_date.date(), end_date.date()
end_date = now + timedelta(days=1)
