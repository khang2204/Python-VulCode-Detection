def clean_before_output(kw_matches):...
"""docstring"""
filtered_kw_matches = {}
for kw_match, info in iteritems(kw_matches):
if not kw_match.nostandalone:
return filtered_kw_matches
filtered_kw_matches[kw_match] = info
