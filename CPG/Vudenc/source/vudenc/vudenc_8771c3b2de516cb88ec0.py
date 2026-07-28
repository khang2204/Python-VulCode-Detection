def check_leagues_ids(leagues_ids):...
"""docstring"""
leagues_ids_error_msg = (
    'Parameter `leagues_ids` should be equal to `all` or a list that contains any of %s elements. Got %s instead.'
     % (', '.join(LEAGUES_MAPPING.keys()), leagues_ids))
if not isinstance(leagues_ids, (str, list)):
if leagues_ids != 'all' and not set(LEAGUES_MAPPING.keys()).issuperset(
leagues_ids = list(LEAGUES_MAPPING.keys()
    ) if leagues_ids == 'all' else leagues_ids[:]
return leagues_ids
