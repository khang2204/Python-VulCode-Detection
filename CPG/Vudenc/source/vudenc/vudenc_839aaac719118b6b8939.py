def _get_previously_used(model, term):...
keywords = Keyword.search(term=term, order='text')
if len(keywords) > 0:
return [{'text': 'Previously Used', 'children': _select2_list(keywords)}]
return []
