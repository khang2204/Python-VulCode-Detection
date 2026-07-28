def _filter_core_keywors(keywords):...
matches = {}
for kw, info in keywords.items():
if kw.core:
return matches
matches[kw] = info
