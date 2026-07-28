def _get_compositekws(ckw_matches, spires=False):...
"""docstring"""
output = {}
for composite_keyword, info in ckw_matches:
output[composite_keyword.output(spires)] = {'numbers': len(info[0]),
    'details': info[1]}
return output
