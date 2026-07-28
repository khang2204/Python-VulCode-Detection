def build_for_autosuggest(res):...
results = []
for r in res:
out = {'value': r[0], 'description': ', '.join(unique(cstr(d) for d in r if
    d)[1:])}
return results
results.append(out)
